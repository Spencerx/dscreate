import os
from os.path import exists
from appdirs import user_data_dir
from typing import List as TypingList
from traitlets.traitlets import MetaHasTraits
from traitlets import Application, List, default, Unicode

# Package objects
from dscreate.utils import GitModel
from .ReadmeCreateApp import ReadmeCreate

dscreate_flags = {
    'local': (
        {'GitModel' : {'push' : False}},
        "Add and commit changes locally without pushing to the remote."
    ),
    'no-stage': (
        {'GitModel' : {'stage': False}},
        "Do not commit changes."
    )
}

class DsCreate(Application):

    name = 'DsCreate'
    flags = dscreate_flags
    description = """
        The base app for dscreate applications.
        This app primarily handles the set up of configuration files for dscreate.

        This app:
        1. Finds the system configuration file / Creates a system configuration file if it does not exist
        2. Finds a configuration file if specified with the `--config_file` argument.
        3. Activates the `.start` method for the traitlets 
           `Application` object which activates the SubApps `.start` method.
        4. Initializes a `.git` attribute
    """

    classes = List()
    app_dir = Unicode()
    config_file_name =  Unicode(config=True, help="Specify a config file to load.")
    system_config_path = Unicode()

    @default('classes')
    def _classes_default(self) -> TypingList[MetaHasTraits]:
        return [GitModel, ReadmeCreate]

    @default("config_file_name")
    def _config_file_name_default(self) -> str:
        return u'dscreate_config.py'

    @default('app_dir')
    def app_dir_default(self) -> str:
        return u'{}'.format(user_data_dir(self.name, 'flatiron'))

    @default('system_config_path')
    def system_config_path_default(self) -> str:
        return u'{}'.format(os.path.join(self.app_dir, self.config_file_name))

    def write_default_config(self) -> None:
        if not exists(self.app_dir):
            os.mkdir(self.app_dir)
        if not exists(self.default_config):
            config = self.generate_config_file()
            if isinstance(config, bytes):
                config = config.decode('utf8')
            with open(self.default_config, 'w+') as file:
                file.write(config)

    def _load_configs(self) -> None:
        self.write_default_config()
        self.load_config_file(self.system_config_path)
        if self.config_file:
            path, config_file_name = os.path.split(self.config_file)
            self.load_config_file(config_file_name, path=path)

    def start(self):
        self._load_configs()
        super(DsCreate, self).start()
        self.git = GitModel()



            

    



    

    

