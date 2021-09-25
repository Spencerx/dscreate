from .BaseApp import DsCreate
from traitlets import default, Unicode
import pyperclip


class ShareApp(DsCreate):

    name = u'dscreate-share'
    description = u'Create a link that opens a github hosted jupyter notebook on github.'


    edit_branch = Unicode(config=True)
    @default('edit_branch')
    def edit_branch_default(self) -> str:
        return 'curriculum'

    def get_file_path(self, url):
        """
        Pull out the organization, repository name, branch, and file path
        from a github url.
        """
        org, repo = url.split('github.com/')[1].split('/')[:2]
        paths = url.split('blob/')[1].split('/')
        branch = paths[0]
        file_path = '/'.join(paths[1:])
        return org, repo, branch, file_path

    def get_assignment_url(self, org, repo, branch, file_path):
        """
        org - The name of a github organization.
        repo - The name of a github repository.
        branch - The name of a github repository branch.
        file_path - The path pointing to a jupyter notebook in a github repository.
        Returns: An illumidesk link that will clone the notebook onto your personal
                server and open the notebook.
        """
        template = """https://flatiron.illumidesk.com/user/x/git-pull?repo=https%3A%2F%2Fgithub.com%2F{}%2F{}&branch={}&subpath={}"""
        return template.format(org, repo, branch, file_path)


    def start(self) -> None:
        super().start()

        if len(self.extra_args) != 1:
            raise ValueError('A github notebook url must be provided.')
        url = self.extra_args[0]
        org, repo, branch, file_path = self.get_file_path(url)
        link = self.get_assignment_url(org, repo, branch, file_path)
        pyperclip.copy(link)
        print('An illumidesk link has been added to your clipboard.')