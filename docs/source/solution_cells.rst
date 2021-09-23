Creating Solution Cells
=======================

What ``ds -create`` is used, all solution cells are removed from the top level ``index.ipynb`` file 
and moved to the ``index.ipynb`` file in the ``.solution_files`` hidden folder. 

Solution cells can be created for both code and Markdown cells in Jupyter Notebooks.

**To create a solution Markdown cell**

Place ``==SOLUTION==`` at the top of a Markdown cell. This tag should have its own line.

**To create a solution code cell**

Place ``#__SOLUTION__`` at the top of the code cell. This tag should have its own line.
