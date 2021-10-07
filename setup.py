from setuptools import setup, find_packages


name = u'dscreate'
version = '0.2.0'
description = 'Flatiron Iron School Data Science Tools'
setup_args = dict(
    name=name,
    version=version,
    description=description,
    author='Joel Collins',
    author_email='joelsewhere@gmail.com',
    license='MIT',
    url='http://github.com/learn-co-curriculum/dscreate',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ds=dscreate.apps.DsCreateApp:main']
    },
install_requires=['argparse', 'pyperclip', 'traitlets', 
                  'nbgrader', 'nbformat', 'nbconvert', 'GitPython',
                  'appdirs'],
)

if __name__ == "__main__":
    setup(**setup_args)