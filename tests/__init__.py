from nbformat.v4 import new_code_cell, new_markdown_cell

class CreateCells:

    def create_code_solution_cell(self):
        source = """#==SOLUTION==
    num = 2 + 2
    num
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

    def create_markdown_solution_cell(self):
        source = """this is a markdown cell"""
        cell = new_markdown_cell(source=source)
        return cell

