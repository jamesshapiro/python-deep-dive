"""
What we've seen so far:

Modules can be imported using
- the import statement
- importlib.import_module()

When a module is imported:
- system cache is checked first (sys.modules)
    - if in cache, just returns the cached reference
    - otherwise:
        - module has to be located (found) somewhere
            - finders (e.g. sys.meta_path)
        - module code has to be retrieved (loaded)
            - loaders (returned by finder -> ModuleSpec)
        - "empty" module typed object is created
        - a reference to the module is added to the system cache (sys.modules)
        - module is compiled (optionally, if not already compiled)
        - module is executed -> sets up the module's namespace (module.__dict__ is module.globals())
"""

"""
Module Finders:
- sys.meta_path
    - _frozen_importlib.BuiltinImporter
        - built-in modules
        - finds built-ins such as "math"
    - _frozen_importlib.FrozenImporter
        - frozen modules
        - a self-contained application that contains everything it needs to run including the Python runtime,
          environment, stdlib, etc. It's not really files, so you need a different importer
    - _frozen_importlib_external.PathFinder
        - file-based modules
        - most common finder after built-ins, what we use to import our own modules and any modules in the
            standard library that are not built-ins
        - PathFinder uses sys.path to find modules and package __path__
"""

"""
built-in
e.g.:
import math

type(math) -> module
math.__spec__ -> ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
math.__name__ -> 'math'
math.__package__ -> ''
__file__ is not an attribute of math (built-ins only)
"""

"""
standard library
import fractions

type(fractions) -> module
fractions.__spec__ -> ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f8b8c0b4a90>, origin='/usr/lib/python3.8/fractions.py')
fractions.__name__ -> 'fractions'
fractions.__package__ -> ''
fractions.__file__ -> '/usr/lib/python3.8/fractions.py'

Note that fractions.__file__ was found by PathFinder in one of the paths listed in sys.path
"""

"""
custom module
import module1

type(module1) -> module
module1.__spec__ -> ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x7f8b8c0b4a90>, origin='/home/james/fake-example-app/module1.py')
module1.__name__ -> 'module1'
module1.__package__ -> ''
module1.__file__ -> '/home/james/fake-example-app/module1.py'

Note that module1.__file__ was found by PathFinder in one of the paths listed in sys.path
"""

"""
Python modules may reside
- in the built-ins
- in files on disk
- they can even be pre-compiled, frozen, or even inside zip archives
- anywhere else that can be accessed by a finder and a loader
    - custom finders/loaders -> databases, http, etc.

For file-based modules (PathFinder):
    They must exist in a path specified in:
        - sys.path
        - or in a path specified by <package>.__path__
"""

