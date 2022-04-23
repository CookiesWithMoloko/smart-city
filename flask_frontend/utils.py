import os
import importlib
def import_dir(module: str):
    for i in os.listdir(f'{module}/'):
        if i.endswith('.py') and i != '__init__.py':
            print(f'import {module}.{i[:-3]}')
            importlib.import_module(f'{module}.{i[:-3]}')
