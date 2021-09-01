from nbgrader.apps import NbGraderAPI
import nbformat
from nbconvert import MarkdownExporter
from traitlets.config.loader import PyFileConfigLoader
from nbconvert.writers import FilesWriter
from traitlets.config import Config
from git import Repo, GitCommandError
import os
import shutil
import sys
import subprocess

def get_top_directory():
    path = os.getcwd()
    split = path.split(os.sep)[::-1]
    if 'source' not in split:
        raise ValueError('ds -generate must be run from an nbgrader assignment folder within the source/ directory.')

    top_directory = ''
    for idx in range(len(split)):
        top_directory = os.path.join(top_directory, '..')
        if split[idx] == 'source':
            break

    return top_directory

def generate_readme(notebook_path, dir_path, filename):
    output_path = os.path.join(dir_path, 'README.md')
    index_files = os.path.join(dir_path, 'index_files')
    input_path = os.path.join(index_files, filename + '.md')
    notebook = nbformat.read(notebook_path, nbformat.NO_CONVERT)
    mark_exporter = MarkdownExporter()
    (output, resources) = mark_exporter.from_notebook_node(notebook)


    if not os.path.isdir(index_files):
        os.mkdir(index_files)
    if os.path.isfile(output_path):
        os.remove(output_path)
    if os.path.isfile(input_path):
        os.remove(input_path)

    c = Config()
    c.FilesWriter.build_directory = index_files
    fw = FilesWriter(config=c)
    fw.write(output, resources, notebook_name=filename)
    shutil.move(input_path, output_path)


class GitModel:

    def __init__(self):
        self.repo =  Repo('.')
        self.msg = self.get_commit_message()

    def get_commit_message(self):
        # get commit message from repo or custom flag
        sys_args = list(sys.argv)
        i = sys_args.index('-m') if '-m' in sys_args else None
        return sys_args[i + 1] if i else self.repo.head.commit.message

    def add_and_commit(self, commit_msg=None):
        self.repo.git.add(".")
        self.repo.git.commit("-m", commit_msg if commit_msg else self.msg)


    def merge_solution(self):
        self.repo.git.checkout('solution')
        solution = self.repo.active_branch
        master = self.repo.branches['master']
        base = self.repo.merge_base(solution, master)
        self.repo.index.merge_tree(master, base=base)
        self.repo.index.commit('Merge master into solution.', parent_commits=(solution.commit, master.commit))


if __name__ == "__main__":

    ASSIGNMENT = os.getcwd().split(os.sep)[-1]

    # create a config object to specify options for nbgrader
    top_directory = get_top_directory()
    config_path = os.path.join(top_directory, 'nbgrader_config.py')
    config_loader = PyFileConfigLoader(config_path)
    config = config_loader.load_config()
    config.pop('IncludeHeaderFooter', None)

    # Connect to api
    api = NbGraderAPI(config=config)

    # Generate Assignment
    print('Generating assignment...')

    results = api.generate_assignment(ASSIGNMENT)
    if not results['success']:
        raise ValueError(results['log'])


    # Generate source readme
    print('Generating source readme...')
    source_path = os.path.join(top_directory, 'source', ASSIGNMENT)
    source_notebook_path = os.path.join(source_path, 'index.ipynb')
    if not os.path.isfile(source_notebook_path):
        raise ValueError('The assignment notebook must be named index.ipynb')
    generate_readme(source_notebook_path, source_path, 'README')

    # Merge into the solution branch
    repo = GitModel()

    if 'solution' not in os.listdir('.git/refs/heads'):
        print('Creating a solution branch...')
        solution = repo.repo.create_head('solution')
        origin = repo.repo.remote()
        origin.push('solution')

    repo.add_and_commit(commit_msg='Update source readme')
    repo.merge_solution()
    repo.repo.git.checkout("master")

    # Create release readme
    print('Generating release readme...')
    release_path = os.path.join(top_directory, 'release', ASSIGNMENT)
    release_notebook_path = os.path.join(release_path, 'index.ipynb')
    generate_readme(release_notebook_path, source_path, 'README')

    print('Pushing changes to master branch...')
    repo.add_and_commit(commit_msg="Update release readme")
    repo.repo.git.push("origin", "master")
    repo.repo.git.checkout("solution")
    print('Pushing changes to solution branch...')
    repo.repo.git.push("origin", "solution")
    repo.repo.git.checkout('master')