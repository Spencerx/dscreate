-------------
CLI Tools
-------------

-------------
``ds -begin``
-------------
When this command is run the following things happen:

* A ``data/`` folder is added to the current working directory
* A ``.solution_files`` subdirectory is added to the current working directory
* A ``curriculum.ipynb`` file is added to the current working directory
   
   * This notebook contains instructions for creating solution tags. See `Creating Solution Cells <#solution-cells>`_.
   * All curriculum content needs to be created in this file in order to use ``ds -create``.


-------------
``ds -create``
-------------
When this command is run the following things happen:

- An ``index.ipynb`` file is added to the current working directory containing all "student facing" content within the ``curriculum.ipynb`` file
- An ``index.ipynb`` file is added to the ``.solution_files`` subdirectory containing all solution content in the ``curriculum.ipynb`` file.
- The ``curriculum.ipynb`` file is deleted
   
   - To make future edits to this project, the curriculum notebook must be generated using `ds -edit`.


-------------
``ds -edit``
-------------
When this command is run the following things happen:

* The metadata inside the lesson and solution notebooks are used to recompile the ``curriculum.ipynb`` notebook.

Once the curriculum notebook is compiled, edits to the lesson can be made inside ``curriculum.ipynb``.
Once edits are complete, run ``ds -create`` to hide the solutions inside a hidden folder.


-------------
``ds -share <Github notebook url>``
-------------

* This command accepts any link that points to a public notebook on github. When this command is run, a link is copied to your clipboard that points to the notebook on illumidesk.
* This command can be used to create `url module items in canvas <https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-add-an-external-URL-as-a-module-item/ta-p/967>`_.

-------------------------------------------------------