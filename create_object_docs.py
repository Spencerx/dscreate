from dscreate import apps, pipeline
import inspect
import os
from types import FunctionType
from dscreate import apps, pipeline

def create_class_docs(dsobject):
    name = dsobject.__name__
    description = dsobject.description
    configs = dsobject.class_config_rst_doc()
    
    doc = f'''{name}\n----------------------------\n{description}\n{configs}'''
    
    return doc

def create_method_docs(dsobject):
    name = dsobject.__name__
    args = str(inspect.signature(dsobject))
    doc = dsobject.__doc__
    
    return f"**{name}**\n\n``{name}{args}:``\n\n{doc}\n\n"
    

def create_dsobject_docs():
    modules = {
              pipeline: pipeline.__all__}
    
    docs = '==================\nCode Documentation\n==================\n\n'
    
    for module in modules:
        objects = modules[module]
        for obj_name in objects:
            obj = getattr(pipeline, obj_name)
            obj_docs = create_class_docs(obj)
            docs += obj_docs
            methods = []
            for key in obj.__dict__:
                if type(obj.__dict__[key]) == FunctionType:
                    methods.append(obj.__dict__[key])
            for method in methods:
                docs += create_method_docs(method)
    return docs

if __name__ == '__main__':
    docs  = create_dsobject_docs()
    doc_path = os.path.join('docs', 'source', 'pages', 'code_documentation.rst')
    file = open(doc_path, 'w+')
    file.write(docs)
    file.close()
