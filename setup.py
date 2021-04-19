from setuptools import setup

setup(name='dscreate',
      version='0.1',
      description='Flatiron Iron School Data Science Tools',
      url='http://github.com/learn-co-curriculum/dscreate',
      author='Joél Collins',
      author_email='@joelsewhere',
      license='MIT',
      packages=['dscreate'],
      install_requires=['argparse', 'pyperclip'],
      scripts=['bin/ds'],
      zip_safe=False)