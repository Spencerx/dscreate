----------
Pipeline
----------

DsPipeline
----------------------------

    The primary pipeline for dscreate

    DsPipeline's primary variable is ``steps`` containing converter and controller objects.
    Every object included in steps must have ``enabled`` and ``printout`` attributes, and a ``.start``  method
    
DsPipeline.branches : List
    Default: ``[]``

    No description

DsPipeline.steps : List
    Default: ``[]``

    No description
**__init__**

``__init__(self, **kwargs) -> None:``


        Set up configuration file.
        

**start**

``start(self) -> None:``

No description

CollectCurriculum
----------------------------

    CollectCurriculum reads in the edit_file and stores the notebook in the application
    configuration object.
    
CollectCurriculum.edit_branch : Unicode
    Default: ``''``

    No description

CollectCurriculum.edit_file : Unicode
    Default: ``''``

    No description
**start**

``start(self) -> None:``

No description

----------
Controllers
----------

BaseController
----------------------------

    The base controller object. 

    **Behavior:**

    This object is used to configure git repository controller objects.

    Primarily, controllers inherit ``enabled`` and ``branches`` attributes from the BaseController.

    ``enabled``
    * When enabled is true, the controller is used during the notebook split
    
BaseController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

BaseController.enabled : Bool
    Default: ``False``

    No description
**__init__**

``__init__(self, **kwargs) -> None:``


        1. Set up configuration file.
        2. Inherit git repo attributes
        

CheckoutController
----------------------------

    Checkout branches set by the running application.

    This controller relies on a configuration object that contains the following variables

    * ``BaseController.branches``
    * ``CommitController.count

    The commit controller count is added to the config object if it does not exist, but does not increment the count. 
    The count variable is used to identify the next branch in the BaseController.branches sequence.

    dscreate uses a "force" merge strategy which overwrites each branch with the most recent edit branch commit.
    It is equivalent to running ``git merge <name of branch> -X theirs``
    
CheckoutController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CheckoutController.enabled : Bool
    Default: ``False``

    No description

CheckoutController.printout : Unicode
    Default: ``''``

    No description
**get_branch**

``get_branch(self):``

No description

**merge_edit_branch**

``merge_edit_branch(self):``

No description

**start**

``start(self) -> None:``

No description

CommitController
----------------------------

    Commits changes to a git branch.

    This object has a ``commit_msg`` attribute that can be set from command line using the ``-m`` argument.

    If a commit message is not provided the commit message defaults to 'Updating  <name of branch>'

    
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
**add_and_commit**

``add_and_commit(self, commit_msg=None):``

No description

**start**

``start(self) -> None:``

No description

PushController
----------------------------

    Pushing changes to the remote.

    Remote is a configurable variables that defaults to 'origin'
    
PushController.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

PushController.enabled : Bool
    Default: ``False``

    No description

PushController.remote : Unicode
    Default: ``''``

    No description
**get_branch**

``get_branch(self):``

No description

**start**

``start(self) -> None:``

No description

CheckoutEditBranch
----------------------------

    This controller checkouts the first branch of the branches configuration variable.
    
CheckoutEditBranch.branches : List
    Default: ``['curriculum', 'master', 'solution']``

    No description

CheckoutEditBranch.enabled : Bool
    Default: ``False``

    No description
**start**

``start(self) -> None:``

No description

----------
Converters
----------

BaseConverter
----------------------------

    The base converter that is inherited by all dscreate converters.

    The base converter initializes and activates the exporter and filewriter objects.
    If the  ``--inline`` flag is used with ``ds create``, a `.solution_dir` directory is created.

    The base converter has an ``--output`` argument that allows you to change the name of the output file. 
    This variable defaults to ``'index'``

    When the base converter is used a step in the pipeline, the edit_file is written to disk unchanged.
    
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
**__init__**

``__init__(self, **kwargs: Any) -> None:``


        Set up configuration file.
        

**start**

``start(self) -> None:``


        Activate the converter
        

**_init_preprocessors**

``_init_preprocessors(self) -> None:``


        Here we add the preprocessors to the exporter pipeline
        with the `register_preprocessor` method.
        

**convert_notebook**

``convert_notebook(self) -> None:``


        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

**init_notebook_resources**

``init_notebook_resources(self) -> dict:``


        The resources argument, when passed into an exporter,
        tell the exporter what directory to include in the url 
        for external images via `output_files_dir`. 

        The `output_name` value is required by nbconvert and is typically 
        the name of the original notebook.
        

**write_notebook**

``write_notebook(self, output, resources) -> None:``


        Sets the output directory for the file write
        and writes the file to disk. 
        

MasterConverter
----------------------------

    The master converter is used to generate the student facing notebook.

    The preprocessors default to the nbconvert ClearOutput and dscreate RemoveSolutions preprocessors.
    
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
**start**

``start(self) -> None:``

No description

ReleaseConverter
----------------------------

    ReleaseConverter replicates ``nbgrader generate``
    
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
**convert_notebook**

``convert_notebook(self) -> None:``


        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

SolutionConverter
----------------------------

    SolutionConverter generates the teacher facing  notebook.
    
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
**start**

``start(self) -> None:``

No description

ReadmeConverter
----------------------------

    Generates the readme for a notebook.

    This converter has a ``notebook_path`` configurable variable that indicates what notebook should be converted.
    notebook_path defaults to 'index.ipynb' when ``--inline`` is False and ``.solution_files/index.ipynb`` when
    ``--inline`` is True.

    No preprocessors are applied by the ReadmeConverter.
    
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
**convert_notebook**

``convert_notebook(self) -> None:``


        1. Create a resources object that tells the exporter how to format link urls for images.
        2. Pass the notebook through the preprocessor and convert to the desired format via the exporter.
        3. Write the notebook to file.
        

SourceConverter
----------------------------

    SourceConverter generates a teacher facing readme for an nbgrader assignment.
    
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
----------
Preprocessors
----------

AddCellIndex
----------------------------

    AddCellIndex adds a metadata.index variable to a notebook and determines if a cell is a solution cell.
    This preprocessor is used primarily for ``--inline`` splits.
    
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
**preprocess**

``preprocess(self, nb, resources):``

No description

**preprocess_cell**

``preprocess_cell(self, cell, resources, cell_index):``


        No transformation is applied.
        

RemoveSolutions
----------------------------

    RemoveSolutions removes cells that contain a solution tag. 

    This preprocess identifies both code and solution cells:

    code solution tags defaults to: {'#__SOLUTION__', '#==SOLUTION=='}
    markdown solution tags defaults to: {'==SOLUTION==','__SOLUTION__'}
    
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
**is_code_solution**

``is_code_solution(self, cell):``


        Checks that a cell has a tag that is to be removed
        Returns: Boolean.
        True means cell should *not* be removed.
        

**is_markdown_solution**

``is_markdown_solution(self, cell):``

No description

**preprocess**

``preprocess(self, nb, resources):``

No description

RemoveLessonCells
----------------------------

    RemoveLessonCells removes cells that do not contain a tag included in the ``solution_tags`` variable.

    ``solution_tags`` are a  configurable variable. Defaults to {'#__SOLUTION__', '#==SOLUTION==', '__SOLUTION__', '==SOLUTION=='}
    
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
**is_solution**

``is_solution(self, cell):``


        Checks that a cell has a solution tag. 
        

**preprocess**

``preprocess(self, nb, resources):``

No description

**preprocess_cell**

``preprocess_cell(self, cell):``


        Removes the solution tag from the solution cells.
        

SortCells
----------------------------

    Sorts the cells of a notebook according to the metadata.index variable
    and adds a solution tag back to solution cells.
    
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
**preprocess**

``preprocess(self, nb, resources):``

No description

**preprocess_cell**

``preprocess_cell(self, cell, resources, cell_index):``

No description

ClearOutput
----------------------------

    ClearOutput removes the outputs for notebook cells.
    
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
ExecuteCells
----------------------------

    ExecuteCells runs code cells in a notebook.
    
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

