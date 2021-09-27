from nbformat.v4 import new_code_cell, new_markdown_cell

class CreateCells:

    def create_code_solution_cell(self):
        source = """#==SOLUTION==
num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_code_solution_cell_tag_location(self):
        source = """num = 2 + 2
num
#==SOLUTION==
"""
        cell = new_code_cell(source=source)
        return cell

    def create_code_solution_cell_tag_shared_line(self):
        source = """num = 2 + 2
num
#==SOLUTION==
"""
        cell = new_code_cell(source=source)
        return cell

    def create_code_lesson_cell(self):
        source = """num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_markdown_solution_cell(self):
        source = """==SOLUTION==
this is a markdown cell
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_markdown_solution_cell_tag_location(self):
        source = """this is a markdown cell

==SOLUTION==
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_markdown_solution_cell_tag_location(self):
        source = """this is a markdown cell

==SOLUTION==
        """
        cell = new_markdown_cell(source=source)
        return cell

    def create_code_solution_cell_config_tag(self):
        source = """#==ANSWER==
num = 2 + 2
num
    """
        cell = new_code_cell(source=source)
        return cell

    def create_markdown_solution_cell_config_tag(self):
        source = """==ANSWER==
this is a markdown cell
        """
        cell = new_markdown_cell(source=source)
        return cell

