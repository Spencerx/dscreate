import os
import logging
from os.path import exists
from appdirs import user_data_dir
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from traitlets import  List, default, Unicode, Bool, Integer
from traitlets.config import Application, Config

# Package objects
from dscreate.utils import GitModel
from .. import pipeline

dscreate_flags = {
    'local': (
        {'PushController' : {'enabled' : False}},
        "Create assignment, add, and commit changes locally without pushing to the remote."
    ),
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

        *Behavior:*

        1. The first time a dscreate CLI app is activated, the system configuration directory is created using
           the ``appdirs`` python package.
        2. A subdirectory called ``ds`` is created and a ``dscreate_config.py`` file
           is added to the ``ds`` subdirectory. This serves as the global configuration file for dscreate. 
        3. A subdirectory for the activated application is created inside the system configuration directory.
        4. A ``dscreate_config.py`` file is added to the application subdirectory. This serves as a localized configuration
           file for a specific dscreate application.
        5. If the configuration directories already exist, the configuration files are loaded into a ``traitlets`` config
           object which will be used to alter the settings of the application components.
        6. Additional configuration files can be used if specified with the ``--config_file`` argument.
        7. The traitlets ``Application.start`` method is activated, which in turn activates the  sub application's
           ``.start``  method.
    """

    classes = List(config=True)
    config_file = Unicode(config=True)
    config_file_name = Unicode(u'dscreate_config.py', 
                               help="Specify a config file to load.").tag(config=True)
    log_level = Integer(logging.CRITICAL).tag(config=True)

    dsconfig = Unicode(config=True)
    @default('dsconfig')
    def dsconfig_default(self) -> str:
        return user_data_dir('dscreate')
    
    app_dir = Unicode(config=True)
    @default('app_dir')
    def app_dir_default(self) -> str:
        return os.path.join(self.dsconfig, self.name)

    @default('classes')
    def _classes_default(self) -> TypingList[MetaHasTraits]:
        return self.all_configurable_classes()

    def all_configurable_classes(self) -> TypingList[MetaHasTraits]:
        """Get a list of all configurable classes for dscreate
        """
        classes = [DsCreate]

        for _, (app, _) in self.subcommands.items():
            if len(app.class_traits(config=True)) > 0:
                classes.append(app)

        for pp_name in pipeline.__all__:
            pp = getattr(pipeline, pp_name)
            if pp.class_traits(config=True):
                classes.append(pp)

        return classes

    system_config_path = Unicode(config=True)
    @default('system_config_path')
    def system_config_path_default(self) -> str:
        return u'{}'.format(os.path.join(self.app_dir, self.config_file_name))

    def write_default_config(self) -> None:
        if not exists(self.dsconfig):
            os.mkdir(self.dsconfig)
        if not exists(self.app_dir):
            os.mkdir(self.app_dir)
        if not exists(self.system_config_path):
            config = self.generate_config_file()
            if isinstance(config, bytes):
                config = config.decode('utf8')
            with open(self.system_config_path, 'w+') as file:
                file.write(config)

    def _load_configs(self) -> None:
        self.add_all_configurables()
        if not exists(self.system_config_path):
            self.write_default_config()
        self.load_config_file(self.system_config_path)
        if self.config_file:
            path, config_file_name = os.path.split(self.config_file)
            self.load_config_file(config_file_name, path=path)
        self.config.merge(self.cli_config)

    def add_all_configurables(self):

        for _, (app, _) in self.subcommands.items():
            traits = app.class_traits(config=True)
            for trait in traits:
                config = Config({app.__class__.__name__: Config({trait : traits[trait].default_value})})
                self.config.merge(config)

        for pp_name in pipeline.__all__:
            pp = getattr(pipeline, pp_name)
            traits = pp.class_traits(config=True)
            for trait in traits:
                config = Config({pp.__class__.__name__: Config({trait : traits[trait].default_value})})
                self.config.merge(config)

    def start(self):
        super(DsCreate, self).start()
        self._load_configs()
        



            

    



    

    

