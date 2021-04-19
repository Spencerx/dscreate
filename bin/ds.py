"""
File for running the `ds` instructor tools.
"""

from dscreate import *
import argparse

parser = argparse.ArgumentParser(description='Flatiron Data Science Instructor Tools')
parser.add_argument('-begin', action='store_true', default=False, dest='begin')
parser.add_argument('-create', action='store_true', default=False, dest='create',
                    help='Split curriculum notebook into lesson and solution notebooks.')

parser.add_argument('-share', action="store", dest='url',
                    help='''Adds a link to your clipboard that opens any public github notebook
                            in illumidesk.''')


color = Color()                            
args = parser.parse_args()
if args.begin:
    begin()
    print(color.BOLD, color.CYAN, '💻 Lesson directory created! Curriculum materials should be developed in the curriculum.ipynb file!', color.END)
if args.create:
    splitter = SplitNotebook()
    splitter.main()
    print()
    print(color.BOLD, color.CYAN, '📒 Solution and Lesson Notebooks have been created!', color.END)
    print()
    
if args.url:
    share = ShareNotebook()
    share.main(args.url)
    print()
    print(color.BOLD, color.CYAN, '📋 An Illumidesk link has been added to your clipboard!', color.END)
    print()