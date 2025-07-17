import pkgutil
import importlib

AGENTS = {}

for module_info in pkgutil.iter_modules(__path__):
    if module_info.name.endswith("_agent"):
        module = importlib.import_module(f".{module_info.name}", package=__name__)
        for name in dir(module):
            attr = getattr(module, name)
            if callable(attr) and name.endswith("_agent"):
                AGENTS[name] = attr
