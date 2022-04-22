import os
import importlib
import colorama
colorama.init()
module = 'tests'
print('\n'*5)
print('='*30)
print('Tests')
print('='*30)

for i in os.listdir(f'{module}/'):
    if i.endswith('.py') and i != '__init__.py':

        s = None
        try:
            importlib.import_module(f'{module}.{i[:-3]}')
            s = True
        except AssertionError:
            s = False
        r = {
            True: colorama.Fore.GREEN,
            False: colorama.Fore.RED,
            None: colorama.Fore.YELLOW
        }
        print(
            f'{module}.{i[:-3]} : {r[s]}{s}{colorama.Fore.RESET}'
        )
print('='*30, '\n\n')
