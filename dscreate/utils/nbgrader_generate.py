import nbformat
from traitlets.config import Config
from nbconvert.writers import FilesWriter
from nbconvert.exporters import NotebookExporter
from nbgrader.preprocessors import (ClearSolutions,
                                    LockCells,
                                    ComputeChecksums,
                                    CheckCellMetadata,
                                    ClearOutput,
                                    ClearHiddenTests,
                                    ClearMarkScheme)

def nbgrader_generate(notebook_path):
    # Read in the notebook
    notebook = nbformat.read(notebook_path, as_version=4)

    # Set up the config
    c = Config()
    c.NotebookExporter.preprocessors = [ClearSolutions,
                                        LockCells,
                                        ComputeChecksums,
                                        CheckCellMetadata,
                                        ClearOutput,
                                        ClearHiddenTests,
                                        ClearMarkScheme]

    # Convert the notebook
    exporter = NotebookExporter(config=c)
    return exporter.from_notebook_node(notebook)

    # Convert the notebook
    exporter = NotebookExporter(config=c)
    return exporter.from_notebook_node(notebook)