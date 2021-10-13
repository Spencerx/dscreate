import tempfile
import io
import os
import pytest
import shutil    
from git import Repo
from traitlets import HasTraits, List
from traitlets.config import Config
from nbformat import read
from .. import CreateCells, LoadNotebooks

class BaseTestConverter(CreateCells, LoadNotebooks):

    required_attributes = ['description',
                            'preprocess',
                            'enabled']


    @pytest.fixture
    def git_remote(self, tmp_path):
        d = tmp_path / ".git"
        d.mkdir()
        repo = Repo.init(d, bare=True)
        return d

    @pytest.fixture
    def dir_test(self, tmp_path, git_remote):
        d = tmp_path / 'repo'
        d.mkdir()
        cloned_repo = Repo.clone_from(git_remote, d)
        remote = cloned_repo.create_remote('test', url=self.repo_test())
        remote.fetch()
        cloned_repo.git.checkout('curriculum')
        cloned_repo.git.remote('rm', 'test')

        return d

    def repo_test(self):
        return 'https://github.com/learn-co-curriculum/dscreate-create-test.git'

    @pytest.fixture
    def config(self, dir_test):
        os.chdir(dir_test)
        with io.open(f'index.ipynb', mode="r", encoding="utf-8") as file:
            nb = read(file, as_version=4)
        c = Config()
        c.source_notebook = nb
        c.inline = Config()
        c.inline.enabled = False
        c.inline.solution = False
        return c

