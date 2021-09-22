from traitlets.config import Configurable
from traitlets import Unicode, default
import nbformat


class CollectCurriculum(Configurable):

    name = 'collect-curriculum'
    
    edit_file = Unicode(config=True)
    @default('edit_file')
    def edit_file_default(self) -> str:
        return 'index.ipynb'

    edit_branch = Unicode(config=True)
    @default('edit_branch')
    def edit_branch_default(self) -> str:
        return 'curriculum'


    def start(self) -> None:
        notebook = nbformat.read(self.edit_file, as_version=4)
        self.config.source_notebook = notebook


