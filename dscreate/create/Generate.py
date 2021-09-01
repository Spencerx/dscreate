# Manage file system
import os
import sys
import shutil

# Notebook APIs
import nbformat
from nbgrader.apps import NbGraderAPI
from nbconvert import MarkdownExporter
from nbconvert.writers import FilesWriter
from traitlets.config import Config
from traitlets.config.loader import PyFileConfigLoader

# Git API
from git import Repo, GitCommandError

def get_top_directory():
    """
    Helper function for finding the top level directory of an nbgrader course.

    This function searches for the word 'source' in the absolute path of the current working directory, and uses the
    placement of the source folder to find the top level of the nbgrader course

    Returns: str. directory path.
    """

    # Get current working directory
    path = os.getcwd()
    # Split and reverse the cwd path
    split = path.split(os.sep)[::-1]
    if 'source' not in split:
        raise ValueError('ds -generate must be run from an nbgrader assignment folder within the source/ directory.')
    # Move up a directory for each directory beneath and equal to the source directory
    top_directory = ''
    for idx in range(len(split)):
        top_directory = os.path.join(top_directory, '..')
        if split[idx] == 'source':
            break

    return top_directory

def generate_readme(notebook_path, dir_path, filename):
    """
    Saves a jupyter notebook as a README.md file using nbformat and nbconvert

    Inputs:
    1. The path for a jupyter notebook to be converted into markdown. str.
    2. The directory path for saving the README.md file. str.
    3. The name of the file without the `.filetype` (README instead of README.md). str.

    Returns:
    None
    """
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


class GitModel(Repo):

    def __init__(self):
        Repo.__init__(self, '.')
        self.msg = self.get_commit_message()

    def get_commit_message(self):
        # get commit message from repo or custom flag
        sys_args = list(sys.argv)
        i = sys_args.index('-m') if '-m' in sys_args else None
        return sys_args[i + 1] if i else self.head.commit.message

    def add_and_commit(self, commit_msg=None):
        self.git.add(".")
        try:
            self.git.commit("-m", commit_msg if commit_msg else self.msg)
        except GitCommandError:
            print("nothing to commit, working tree clean")

    def merge_solution(self):
        self.git.checkout('solution')
        solution = self.active_branch
        master = self.branches['master']
        base = self.merge_base(solution, master)
        self.index.merge_tree(master, base=base)
        self.index.commit('Merge master into solution.', parent_commits=(solution.commit, master.commit))


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
    # Save source readme to master branch
    generate_readme(source_notebook_path, source_path, 'README')

    # Create a git interface
    repo = GitModel()

    # Create a solution branch if it doesn't exist
    if 'solution' not in os.listdir('.git/refs/heads'):
        print('Creating a solution branch...')
        solution = repo.create_head('solution')
        origin = repo.remote()
        origin.push('solution')

    # Commit changes to master branch
    repo.add_and_commit(commit_msg='Update source readme')
    
    # Merge master into solution
    repo.merge_solution()

    # Checkout master branch
    repo.git.checkout("master")

    # Create release readme
    print('Generating release readme...')
    release_path = os.path.join(top_directory, 'release', ASSIGNMENT)
    release_notebook_path = os.path.join(release_path, 'index.ipynb')

    # Save release readme to master branch
    generate_readme(release_notebook_path, source_path, 'README')

    # Commit changes to master branch
    repo.add_and_commit(commit_msg="Update release readme")

    # Push changes
    print('Pushing changes to master branch...')
    repo.git.push("origin", "master")
    repo.git.checkout("solution")
    print('Pushing changes to solution branch...')
    repo.git.push("origin", "solution")

    # End on master branch
    repo.git.checkout('master')