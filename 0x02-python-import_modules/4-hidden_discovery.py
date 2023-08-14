import importlib.util

module_spec = importlib.util.spec_from_file_location("hidden_4", "/Users/mwihaki/alx/alx-higher_level_programming/0x02-python-import_modules/hidden_4.pyc")
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)

names = [name for name in dir(module) if not name.startswith('__')]
names.sort()

for name in names:
    print(name)