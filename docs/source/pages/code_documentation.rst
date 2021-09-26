----------
Apps
----------

DsCreate
----------------------------

.. admonition::

   
        The base app for dscreate applications.
        This app primarily handles the set up of configuration files for dscreate.

        *Behavior:*

        1. The first time a dscreate CLI app is activated, the system configuration directory is created using
           the ``appdirs`` python package.
        2. A subdirectory called ``ds`` is created and a ``dscreate_config.py`` file
           is added to the ``ds`` subdirectory. This serves as the global configuration file for dscreate. 
        3. A subdirectory for the activated application is created inside the system configuration directory.
        4. A ``dscreate_config.py`` file is added to the application subdirectory. This serves as a localized configuration
           file for a specific dscreate application.
        5. If the configuration directories already exist, the configuration files are loaded into a ``traitlets`` config
           object which will be used to alter the settings of the application components.
        6. Additional configuration files can be used if specified with the ``--config_file`` argument.
        7. The traitlets ``Application.start`` method is activated, which in turn activates the  sub application's
           ``.start``  method.
    

**CONFIGURABLE VARIABLES:**

DsCreate.app_dir : Unicode
    Default: ``''``

    No description

DsCreate.classes : List
    Default: ``[]``

    No description

DsCreate.config_file : Unicode
    Default: ``''``

    No description

DsCreate.config_file_name : Unicode
    Default: ``'dscreate_config.py'``

    Specify a config file to load.

DsCreate.dsconfig : Unicode
    Default: ``''``

    No description

DsCreate.log_datefmt : Unicode
    Default: ``'%Y-%m-%d %H:%M:%S'``

    The date format used by logging formatters for %(asctime)s

DsCreate.log_format : Unicode
    Default: ``'[%(name)s]%(highlevel)s %(message)s'``

    The Logging format template

DsCreate.log_level : Int
    Default: ``50``

    No description

DsCreate.show_config : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout

DsCreate.show_config_json : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout (as JSON)

DsCreate.system_config_path : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: all_configurable_classes(self) -> List[traitlets.traitlets.MetaHasTraits]:

   Get a list of all configurable classes for dscreate
        

.. admonition:: write_default_config(self) -> None:

   No description

.. admonition:: _load_configs(self) -> None:

   No description

.. admonition:: add_all_configurables(self):

   No description

.. admonition:: start(self):

   No description

CreateApp
----------------------------

.. admonition::

   
    Splits a notebook into student and teacher facing materials using dscreate solution tags.
    
    **Behavior:**

    CreateApp uses three major variables.

    1. ``pipeline_steps``
        * This variable is a list containing the converters and controllers that are applied to the repository.
    2. ``branches``
        * This variable is a list containing the name of git branches and is used by CheckoutControllers (included in the ``pipeline_steps`` list) to move sequentially across the branches.
        * *It is worth noting that the ``pipeline_steps`` list cannot contain more CheckoutControllers than the length of ``branches``.
    3. ``inline``
        * This variable is a bool that indicates whether or not to split the notebooks on solely on the active branch. When inline is True, the solution files are stored in a ``.solution_files`` directory.
        * inline is set to True via the ``--inline`` flag.
        * When inline is true, a ``curriculum.ipynb`` file used as the ``edit_file``.

    - If a branch inside the branches list has not been created, it is created.
    - For notebook splits that requires git branches, the application must be run from the edit_branch which defaults to ``curriculum``.
    

**CONFIGURABLE VARIABLES:**

CreateApp.app_dir : Unicode
    Default: ``''``

    No description

CreateApp.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CreateApp.classes : List
    Default: ``[]``

    No description

CreateApp.config_file : Unicode
    Default: ``''``

    No description

CreateApp.config_file_name : Unicode
    Default: ``'dscreate_config.py'``

    Specify a config file to load.

CreateApp.dsconfig : Unicode
    Default: ``''``

    No description

CreateApp.edit_branch : Unicode
    Default: ``'curriculum'``

    No description

CreateApp.inline : Bool
    Default: ``False``

    No description

CreateApp.log_datefmt : Unicode
    Default: ``'%Y-%m-%d %H:%M:%S'``

    The date format used by logging formatters for %(asctime)s

CreateApp.log_format : Unicode
    Default: ``'[%(name)s]%(highlevel)s %(message)s'``

    The Logging format template

CreateApp.log_level : Int
    Default: ``50``

    No description

CreateApp.pipeline_steps : List
    Default: ``[]``

    No description

CreateApp.show_config : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout

CreateApp.show_config_json : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout (as JSON)

CreateApp.system_config_path : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: validate_branches(self) -> None:

   No description

.. admonition:: start(self) -> None:

   No description

GenerateApp
----------------------------

.. admonition::

   
    Splits an nbgrader assignment into student facing and teacher facing files
    and uses the arguments to determine which sub application should be activated.

    **Behavior:**

    GenerateApp uses three major variables.

    1. ``pipeline_steps``
        * This variable is a list containing the converters and controllers that are applied to the repository.
    2. ``branches``
        * This variable is a list containing the name of git branches and is used by CheckoutControllers (included in the ``pipeline_steps`` list) to move sequentially across the branches.
        * *It is worth noting that the ``pipeline_steps`` list cannot contain more CheckoutControllers than the length of ``branches``.
    
    This app uses nbgrader's preprocessors to create student facing and and teacher facing versions for the README markdown files. 
    The curriculum notebook is saved to each branch. 
    

**CONFIGURABLE VARIABLES:**

GenerateApp.app_dir : Unicode
    Default: ``''``

    No description

GenerateApp.branches : List
    Default: ``['master', 'solution']``


    Sets the branches used for the notebook  split.
    Default: ['master', 'solution']


GenerateApp.classes : List
    Default: ``[]``

    No description

GenerateApp.config_file : Unicode
    Default: ``''``

    No description

GenerateApp.config_file_name : Unicode
    Default: ``'dscreate_config.py'``

    Specify a config file to load.

GenerateApp.dsconfig : Unicode
    Default: ``''``

    No description

GenerateApp.edit_branch : Unicode
    Default: ``''``

    Sets the name of the git branch used for curriculum development.
                                      Default: 'curriculum'

GenerateApp.log_datefmt : Unicode
    Default: ``'%Y-%m-%d %H:%M:%S'``

    The date format used by logging formatters for %(asctime)s

GenerateApp.log_format : Unicode
    Default: ``'[%(name)s]%(highlevel)s %(message)s'``

    The Logging format template

GenerateApp.log_level : Int
    Default: ``50``

    No description

GenerateApp.pipeline_steps : List
    Default: ``[]``

    No description

GenerateApp.show_config : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout

GenerateApp.show_config_json : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout (as JSON)

GenerateApp.system_config_path : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: start(self) -> None:

   
        Activates the application.

        * Adds the name of the edit branch to the application configuration object.
        * Configures the DsPipeline object
        * Adds the branches to the controller objects
        * Initializes a DsPipeline
        * Activates thee pipeline
        

ShareApp
----------------------------

.. admonition::

   
    Creates a link that opens a github hosted jupyter notebook on illumidesk.

    **Behavior:**

    * Parses a url that is pointing to a jupyter notebook on github
    * Uses the variables from the parsed url to generate a new url
    * Adds the generated url to the user's clipboard using the python package ``pyperclip``.
    

**CONFIGURABLE VARIABLES:**

ShareApp.app_dir : Unicode
    Default: ``''``

    No description

ShareApp.classes : List
    Default: ``[]``

    No description

ShareApp.config_file : Unicode
    Default: ``''``

    No description

ShareApp.config_file_name : Unicode
    Default: ``'dscreate_config.py'``

    Specify a config file to load.

ShareApp.dsconfig : Unicode
    Default: ``''``

    No description

ShareApp.edit_branch : Unicode
    Default: ``''``

    No description

ShareApp.log_datefmt : Unicode
    Default: ``'%Y-%m-%d %H:%M:%S'``

    The date format used by logging formatters for %(asctime)s

ShareApp.log_format : Unicode
    Default: ``'[%(name)s]%(highlevel)s %(message)s'``

    The Logging format template

ShareApp.log_level : Int
    Default: ``50``

    No description

ShareApp.show_config : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout

ShareApp.show_config_json : Bool
    Default: ``False``

    Instead of starting the Application, dump configuration to stdout (as JSON)

ShareApp.system_config_path : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: get_file_path(self, url):

   
        Pull out the organization, repository name, branch, and file path
        from a github url.
        

.. admonition:: get_assignment_url(self, org, repo, branch, file_path):

   
        org - The name of a github organization.
        repo - The name of a github repository.
        branch - The name of a github repository branch.
        file_path - The path pointing to a jupyter notebook in a github repository.
        Returns: An illumidesk link that will clone the notebook onto your personal
                server and open the notebook.
        

.. admonition:: start(self) -> None:

   No description

----------
Pipeline
----------

DsPipeline
----------------------------

.. admonition::

   
    The primary pipeline for dscreate

    DsPipeline's primary variable is ``steps`` containing converter and controller objects.
    Every object included in steps must have ``enabled`` and ``printout`` attributes, and a ``.start``  method
    

**CONFIGURABLE VARIABLES:**

DsPipeline.branches : List
    Default: ``[]``

    No description

DsPipeline.steps : List
    Default: ``[]``

    No description


**METHODS**

.. admonition:: __init__(self, **kwargs) -> None:

   
        Set up configuration file.
        

.. admonition:: start(self) -> None:

   No description

CollectCurriculum
----------------------------

.. admonition::

   
    CollectCurriculum reads in the edit_file and stores the notebook in the application
    configuration object.
    

**CONFIGURABLE VARIABLES:**

CollectCurriculum.edit_branch : Unicode
    Default: ``''``

    No description

CollectCurriculum.edit_file : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: start(self) -> None:

   No description

----------
Controllers
----------

BaseController
----------------------------

.. admonition::

   
    The base controller object. 

    **Behavior:**

    This object is used to configure git repository controller objects.

    Primarily, controllers inherit ``enabled`` and ``branches`` attributes from the BaseController.

    ``enabled``
    * When enabled is true, the controller is used during the notebook split
    

**CONFIGURABLE VARIABLES:**

BaseController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

BaseController.enabled : Bool
    Default: ``False``

    No description


**METHODS**

.. admonition:: __init__(self, **kwargs) -> None:

   
        1. Set up configuration file.
        2. Inherit git repo attributes
        

CheckoutController
----------------------------

.. admonition::

   
    Checkout branches set by the running application.

    This controller relies on a configuration object that contains the following variables

    * ``BaseController.branches``
    * ``CommitController.count

    The commit controller count is added to the config object if it does not exist, but does not increment the count. 
    The count variable is used to identify the next branch in the BaseController.branches sequence.

    dscreate uses a "force" merge strategy which overwrites each branch with the most recent edit branch commit.
    It is equivalent to running ``git merge <name of branch> -X theirs``
    

**CONFIGURABLE VARIABLES:**

CheckoutController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CheckoutController.enabled : Bool
    Default: ``False``

    No description

CheckoutController.printout : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: get_branch(self):

   No description

.. admonition:: merge_edit_branch(self):

   No description

.. admonition:: start(self) -> None:

   No description

CommitController
----------------------------

.. admonition::

   
    Commits changes to a git branch.

    This object has a ``commit_msg`` attribute that can be set from command line using the ``-m`` argument.

    If a commit message is not provided the commit message defaults to 'Updating  <name of branch>'

    

**CONFIGURABLE VARIABLES:**

CommitController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CommitController.commit_msg : Unicode
    Default: ``''``

    No description

CommitController.count : Int
    Default: ``0``

    No description

CommitController.enabled : Bool
    Default: ``False``

    No description


**METHODS**

.. admonition:: add_and_commit(self, commit_msg=None):

   No description

.. admonition:: start(self) -> None:

   No description

PushController
----------------------------

.. admonition::

   
    Pushing changes to the remote.

    Remote is a configurable variables that defaults to 'origin'
    

**CONFIGURABLE VARIABLES:**

PushController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

PushController.enabled : Bool
    Default: ``False``

    No description

PushController.remote : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: get_branch(self):

   No description

.. admonition:: start(self) -> None:

   No description

CheckoutEditBranch
----------------------------

.. admonition::

   
    This controller checkouts the first branch of the branches configuration variable.
    

**CONFIGURABLE VARIABLES:**

CheckoutEditBranch.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CheckoutEditBranch.enabled : Bool
    Default: ``False``

    No description


**METHODS**

.. admonition:: start(self) -> None:

   No description

----------
Converters
----------

BaseConverter
----------------------------

.. admonition::

   
    The base converter that is inherited by all dscreate converters.

    The base converter initializes and activates the exporter and filewriter objects.
    If the  ``--inline`` flag is used with ``ds create``, a `.solution_dir` directory is created.

    The base converter has an ``--output`` argument that allows you to change the name of the output file. 
    This variable defaults to ``'index'``

    When the base converter is used a step in the pipeline, the edit_file is written to disk unchanged.
    

**CONFIGURABLE VARIABLES:**

BaseConverter.enabled : Bool
    Default: ``False``

    No description

BaseConverter.exporter_class : Type
    Default: ``'nbconvert.exporters.notebook.NotebookExporter'``

    No description

BaseConverter.output : Unicode
    Default: ``''``

    No description

BaseConverter.preprocessors : List
    Default: ``[]``

    No description

BaseConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: __init__(self, **kwargs: Any) -> None:

   
        Set up configuration file.
        

.. admonition:: start(self) -> None:

   
        Activate the converter
        

.. admonition:: _init_preprocessors(self) -> None:

   
        Here we add the preprocessors to the exporter pipeline
        with the `register_preprocessor` method.
        

.. admonition:: convert_notebook(self) -> None:

   
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

.. admonition:: init_notebook_resources(self) -> dict:

   
        The resources argument, when passed into an exporter,
        tell the exporter what directory to include in the url 
        for external images via `output_files_dir`. 

        The `output_name` value is required by nbconvert and is typically 
        the name of the original notebook.
        

.. admonition:: write_notebook(self, output, resources) -> None:

   
        Sets the output directory for the file write
        and writes the file to disk. 
        

MasterConverter
----------------------------

.. admonition::

   
    The master converter is used to generate the student facing notebook.

    The preprocessors default to the nbconvert ClearOutput and dscreate RemoveSolutions preprocessors.
    

**CONFIGURABLE VARIABLES:**

MasterConverter.enabled : Bool
    Default: ``False``

    No description

MasterConverter.exporter_class : Type
    Default: ``'nbconvert.exporters.notebook.NotebookExporter'``

    No description

MasterConverter.output : Unicode
    Default: ``''``

    No description

MasterConverter.preprocessors : List
    Default: ``[]``

    No description

MasterConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: start(self) -> None:

   No description

ReleaseConverter
----------------------------

.. admonition::

   
    ReleaseConverter replicates ``nbgrader generate``
    

**CONFIGURABLE VARIABLES:**

ReleaseConverter.enabled : Bool
    Default: ``False``

    No description

ReleaseConverter.notebook_path : Unicode
    Default: ``''``

    No description

ReleaseConverter.preprocessors : List
    Default: ``[]``

    No description

ReleaseConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: convert_notebook(self) -> None:

   
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

SolutionConverter
----------------------------

.. admonition::

   
    SolutionConverter generates the teacher facing  notebook.
    

**CONFIGURABLE VARIABLES:**

SolutionConverter.enabled : Bool
    Default: ``False``

    No description

SolutionConverter.exporter_class : Type
    Default: ``'nbconvert.exporters.notebook.NotebookExporter'``

    No description

SolutionConverter.output : Unicode
    Default: ``''``

    No description

SolutionConverter.preprocessors : List
    Default: ``[]``

    No description

SolutionConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: start(self) -> None:

   No description

ReadmeConverter
----------------------------

.. admonition::

   
    Generates the readme for a notebook.

    This converter has a ``notebook_path`` configurable variable that indicates what notebook should be converted.
    notebook_path defaults to 'index.ipynb' when ``--inline`` is False and ``.solution_files/index.ipynb`` when
    ``--inline`` is True.

    No preprocessors are applied by the ReadmeConverter.
    

**CONFIGURABLE VARIABLES:**

ReadmeConverter.enabled : Bool
    Default: ``False``

    No description

ReadmeConverter.notebook_path : Unicode
    Default: ``''``

    No description

ReadmeConverter.preprocessors : List
    Default: ``[]``

    No description

ReadmeConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

.. admonition:: convert_notebook(self) -> None:

   
        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

SourceConverter
----------------------------

.. admonition::

   
    SourceConverter generates a teacher facing readme for an nbgrader assignment.
    

**CONFIGURABLE VARIABLES:**

SourceConverter.enabled : Bool
    Default: ``False``

    No description

SourceConverter.notebook_path : Unicode
    Default: ``''``

    No description

SourceConverter.preprocessors : List
    Default: ``[]``

    No description

SourceConverter.solution_dir : Unicode
    Default: ``''``

    No description


**METHODS**

----------
Preprocessors
----------

AddCellIndex
----------------------------

.. admonition::

   
    AddCellIndex adds a metadata.index variable to a notebook and determines if a cell is a solution cell.
    This preprocessor is used primarily for ``--inline`` splits.
    

**CONFIGURABLE VARIABLES:**

AddCellIndex.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

AddCellIndex.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


AddCellIndex.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate

AddCellIndex.solution_tags : Set
    Default: ``{'#==SOLUTION==', '#__SOLUTION__', '==SOLUTION==', '__SOLUTIO...``

    Tags indicating which cells are to be removed


**METHODS**

.. admonition:: preprocess(self, nb, resources):

   No description

.. admonition:: preprocess_cell(self, cell, resources, cell_index):

   
        No transformation is applied.
        

RemoveSolutions
----------------------------

.. admonition::

   
    RemoveSolutions removes cells that contain a solution tag. 

    This preprocess identifies both code and solution cells:

    code solution tags defaults to: {'#__SOLUTION__', '#==SOLUTION=='}
    markdown solution tags defaults to: {'==SOLUTION==','__SOLUTION__'}
    

**CONFIGURABLE VARIABLES:**

RemoveSolutions.code_tags : Set
    Default: ``{'#==SOLUTION==', '#__SOLUTION__'}``

    Tags indicating which cells are to be removed

RemoveSolutions.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

RemoveSolutions.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


RemoveSolutions.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate

RemoveSolutions.markdown_tags : Set
    Default: ``{'==SOLUTION==', '__SOLUTION__'}``

    No description


**METHODS**

.. admonition:: is_code_solution(self, cell):

   
        Checks that a cell has a tag that is to be removed
        Returns: Boolean.
        True means cell should *not* be removed.
        

.. admonition:: is_markdown_solution(self, cell):

   No description

.. admonition:: preprocess(self, nb, resources):

   No description

RemoveLessonCells
----------------------------

.. admonition::

   
    RemoveLessonCells removes cells that do not contain a tag included in the ``solution_tags`` variable.

    ``solution_tags`` are a  configurable variable. Defaults to {'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='}
    

**CONFIGURABLE VARIABLES:**

RemoveLessonCells.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

RemoveLessonCells.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


RemoveLessonCells.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate

RemoveLessonCells.solution_tags : Set
    Default: ``{'#==SOLUTION==', '#__SOLUTION__', '==SOLUTION==', '__SOLUTIO...``

    Tags indicating which cells are to be removed


**METHODS**

.. admonition:: is_solution(self, cell):

   
        Checks that a cell has a solution tag. 
        

.. admonition:: preprocess(self, nb, resources):

   No description

.. admonition:: preprocess_cell(self, cell):

   
        Removes the solution tag from the solution cells.
        

SortCells
----------------------------

.. admonition::

   
    Sorts the cells of a notebook according to the metadata.index variable
    and adds a solution tag back to solution cells.
    

**CONFIGURABLE VARIABLES:**

SortCells.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

SortCells.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


SortCells.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate


**METHODS**

.. admonition:: preprocess(self, nb, resources):

   No description

.. admonition:: preprocess_cell(self, cell, resources, cell_index):

   No description

ClearOutput
----------------------------

.. admonition::

   
    ClearOutput removes the outputs for notebook cells.
    

**CONFIGURABLE VARIABLES:**

ClearOutput.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

ClearOutput.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


ClearOutput.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate

ClearOutput.remove_metadata_fields : Set
    Default: ``{'collapsed', 'scrolled'}``

    No description


**METHODS**

ExecuteCells
----------------------------

.. admonition::

   
    ExecuteCells runs code cells in a notebook.
    

**CONFIGURABLE VARIABLES:**

ExecuteCells.allow_error_names : List
    Default: ``[]``


    List of error names which won't stop the execution. Use this if the
    ``allow_errors`` option it too general and you want to allow only
    specific kinds of errors.


ExecuteCells.allow_errors : Bool
    Default: ``False``


    If ``False`` (default), when a cell raises an error the
    execution is stopped and a `CellExecutionError`
    is raised, except if the error name is in
    ``allow_error_names``.
    If ``True``, execution errors are ignored and the execution
    is continued until the end of the notebook. Output from
    exceptions is included in the cell output in both cases.


ExecuteCells.default_language : Unicode
    Default: ``'ipython'``

    Deprecated default highlight language as of 5.0, please use language_info metadata instead

ExecuteCells.display_data_priority : List
    Default: ``['text/html', 'application/pdf', 'text/latex', 'image/svg+xml...``


    An ordered list of preferred output type, the first
    encountered will usually be used when converting discarding
    the others.


ExecuteCells.enabled : Bool
    Default: ``True``

    Whether to use this preprocessor when running dscreate

ExecuteCells.extra_arguments : List
    Default: ``[]``

    No description

ExecuteCells.force_raise_errors : Bool
    Default: ``False``


    If False (default), errors from executing the notebook can be
    allowed with a ``raises-exception`` tag on a single cell, or the
    ``allow_errors`` or ``allow_error_names`` configurable options for
    all cells. An allowed error will be recorded in notebook output, and
    execution will continue. If an error occurs when it is not
    explicitly allowed, a `CellExecutionError` will be raised.
    If True, `CellExecutionError` will be raised for any error that occurs
    while executing the notebook. This overrides the ``allow_errors``
    and ``allow_error_names`` options and the ``raises-exception`` cell
    tag.


ExecuteCells.interrupt_on_timeout : Bool
    Default: ``False``


    If execution of a cell times out, interrupt the kernel and
    continue executing other cells rather than throwing an error and
    stopping.


ExecuteCells.iopub_timeout : Int
    Default: ``4``


    The time to wait (in seconds) for IOPub output. This generally
    doesn't need to be set, but on some slow networks (such as CI
    systems) the default timeout might not be long enough to get all
    messages.


ExecuteCells.ipython_hist_file : Unicode
    Default: ``':memory:'``

    Path to file to use for SQLite history database for an IPython kernel.

            The specific value ``:memory:`` (including the colon
            at both end but not the back ticks), avoids creating a history file. Otherwise, IPython
            will create a history file for each kernel.

            When running kernels simultaneously (e.g. via multiprocessing) saving history a single
            SQLite file can result in database errors, so using ``:memory:`` is recommended in
            non-interactive contexts.


ExecuteCells.kernel_manager_class : Type
    Default: ``'builtins.object'``

    The kernel manager class to use.

ExecuteCells.kernel_name : Unicode
    Default: ``''``


    Name of kernel to use to execute the cells.
    If not set, use the kernel_spec embedded in the notebook.


ExecuteCells.raise_on_iopub_timeout : Bool
    Default: ``False``


    If ``False`` (default), then the kernel will continue waiting for
    iopub messages until it receives a kernel idle message, or until a
    timeout occurs, at which point the currently executing cell will be
    skipped. If ``True``, then an error will be raised after the first
    timeout. This option generally does not need to be used, but may be
    useful in contexts where there is the possibility of executing
    notebooks with memory-consuming infinite loops.


ExecuteCells.record_timing : Bool
    Default: ``True``


    If ``True`` (default), then the execution timings of each cell will
    be stored in the metadata of the notebook.


ExecuteCells.shell_timeout_interval : Int
    Default: ``5``


    The time to wait (in seconds) for Shell output before retrying.
    This generally doesn't need to be set, but if one needs to check
    for dead kernels at a faster rate this can help.


ExecuteCells.shutdown_kernel : any of ``'graceful'``|``'immediate'``
    Default: ``'graceful'``


    If ``graceful`` (default), then the kernel is given time to clean
    up after executing all cells, e.g., to execute its ``atexit`` hooks.
    If ``immediate``, then the kernel is signaled to immediately
    terminate.


ExecuteCells.startup_timeout : Int
    Default: ``60``


    The time to wait (in seconds) for the kernel to start.
    If kernel startup takes longer, a RuntimeError is
    raised.


ExecuteCells.store_widget_state : Bool
    Default: ``True``


    If ``True`` (default), then the state of the Jupyter widgets created
    at the kernel will be stored in the metadata of the notebook.


ExecuteCells.timeout : Int
    Default: ``None``


    The time to wait (in seconds) for output from executions.
    If a cell execution takes longer, a TimeoutError is raised.

    ``None`` or ``-1`` will disable the timeout. If ``timeout_func`` is set,
    it overrides ``timeout``.


ExecuteCells.timeout_func : Any
    Default: ``None``


    A callable which, when given the cell source as input,
    returns the time to wait (in seconds) for output from cell
    executions. If a cell execution takes longer, a TimeoutError
    is raised.

    Returning ``None`` or ``-1`` will disable the timeout for the cell.
    Not setting ``timeout_func`` will cause the client to
    default to using the ``timeout`` trait for all cells. The
    ``timeout_func`` trait overrides ``timeout`` if it is not ``None``.



**METHODS**

