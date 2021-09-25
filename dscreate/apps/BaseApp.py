import os
from os.path import exists
from appdirs import user_data_dir
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from traitlets import  List, default, Unicode, Bool
from traitlets.config import Application, Config

# Package objects
from dscreate.utils import GitModel
from .. import pipeline

dscreate_flags = {
    'local': (
        {'PushController' : {'enabled' : False}},
        "Create assignment, add, and commit changes locally without pushing to the remote."
    ),
    'inline': (
    {'DsCreate': {'inline': True},
     'CollectCurriculum': {'edit_file': 'curriculum.ipynb'}}, "Create inline directory split.")
}

dscreate_aliases = {
    'push':'PushController.enabled',
    'commit': 'CommitController.enabled',
    'm':'CommitController.commit_msg',
    'execute': 'ExecuteCells.enabled'
    }


class DsCreate(Application):

    name = 'DsCreate'
    aliases = dscreate_aliases
    flags = dscreate_flags
    description = """
        The base app for dscreate applications.
        This app primarily handles the set up of configuration files for dscreate.

        This app:
        1. Finds the system configuration file / Creates a system configuration file if it does not exist
        2. Finds a configuration file if specified with the `--config_file` argument.
        3. Activates the `.start` method for the traitlets 
           `Application` object which activates the SubApps `.start` method.
    """

    classes = List(config=True)
    config_file = Unicode(config=True)
    

    inline = Bool(config=True)
    @default('inline')
    def inline_default(self) -> bool:
        return False

    @default('classes')
    def _classes_default(self) -> TypingList[MetaHasTraits]:
        return [DsCreate]

    def all_configurable_classes(self) -> TypingList[MetaHasTraits]:
        """Get a list of all configurable classes for dscreate
        """
        classes = DsCreate._classes_default(self)

        for _, (app, _) in self.subcommands.items():
            if len(app.class_traits(config=True)) > 0:
                classes.append(app)

        for pp_name in pipeline.__all__:
            pp = getattr(pipeline, pp_name)
            if pp.class_traits(config=True):
                classes.append(pp)

        return classes

    config_file_name =  Unicode(config=True, help="Specify a config file to load.")
    @default("config_file_name")
    def _config_file_name_default(self) -> str:
        return u'dscreate_config.py'

    app_dir = Unicode(config=True)
    @default('app_dir')
    def app_dir_default(self) -> str:
        return u'{}'.format(user_data_dir(self.name, 'flatiron'))

    system_config_path = Unicode(config=True)
    @default('system_config_path')
    def system_config_path_default(self) -> str:
        return u'{}'.format(os.path.join(self.app_dir, self.config_file_name))

    def write_default_config(self) -> None:
        if not exists(self.app_dir):
            os.mkdir(self.app_dir)
        if not exists(self.system_config_path):
            config = self.generate_config_file()
            if isinstance(config, bytes):
                config = config.decode('utf8')
            with open(self.system_config_path, 'w+') as file:
                file.write(config)

    def _load_configs(self) -> None:
        self.write_default_config()
        self.load_config_file(self.system_config_path)
        if self.config_file:
            path, config_file_name = os.path.split(self.config_file)
            self.load_config_file(config_file_name, path=path)


    def start(self):
        super(DsCreate, self).start()
        self._load_configs()
        c = Config()
        c.inline.enabled = self.inline
        c.inline.tracker = int(self.inline)
        self.config.merge(c)
        



            

    



    

    

