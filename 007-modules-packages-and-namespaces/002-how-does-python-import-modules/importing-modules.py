"""
Importing Modules

When we run a statement such as:

import fractions

... what is Python actually doing?

The first thing to note is that Python is doing the import at runtime,
i.e. while your code is actually running.

This is different from traditional compiled languages like C where
modules are compiled and linked at compile time.

In both cases though, the system needs to know where those code files exist.

Python uses a relatively complex system to find and load modules. We
won't even attempt to describe this in detail, but we will take a brief
look at the main points.

The sys module has a few properties that define where Python is going to
look for modules (either built-in or standard library as well as our own
or 3rd party):
"""

import sys

"""
Where is Python installed?
"""

print(f'{sys.prefix=}')

"""
Where are the compiled C binaries located?
"""
print(f'{sys.exec_prefix=}')

"""
These two properties are how virtual environments are basically able to
work with different environments. Python is installed to a different
set of directories, and these prefixes are manipulated to reflect the
current Python location.
"""

"""
Where does Python look for imports?
"""
print(f'{sys.path=}')

"""
Basically, when we import a module, Python will search for the module
in the paths contained in sys.path.

If it does not find the module in one of those paths, the import will fail.

So if you ever run into a problem where Python is not able to import a
module or package, you should check this first to make sure that the
path to your module/package is in that list.

At a high level, this is how Python imports a module from file:
- checks the sys.modules cache to see if the module has already been imported.
  If so, it simply uses the reference in there, otherwise:
- creates a new module object (types.ModuleType)
- loads the source code from file
- adds an entry to sys.modules with name as key
- compiles and executes the source code

One thing that's really important to note is that when a module is
imported, the module code is executed.
"""

"""
Example 1:

This example shows that when we import a module, the module code is
actually executed.

Furthermore, that module now has its own namespace that can be seen in __dict__.
"""

"""
Example 2:

In this example, we can see that when we import a module, Python first looks
for it in sys.modules.

To make the point, we put a key/value pair in sys.modules ourselves, and then
import it.

In fact, we put a function in there instead of a module, and import that.

Please DO NOT do this, we're just making the point that import will first look
in the cache and immediately just return the object if the name is found,
basically just as if we had written:

module = sys.modules['module']
import test

See, it got the "module" from sys...
"""

import sys
sys.modules['test'] = lambda: 'Testing module caching'

import test
print(f'{test()=}')

"""
Example 3a:

In this example, we look at a simplified view of how Python imports a module.

We use two built-in functions, compile and exec.

The compile function compiles source (e.g. text) into a code object.

The exec function is used to execute a code object. Optionally, we can specify
what dictionary should be used to store global symbols.

In our case, we are going to want to use our module's __dict__.
"""

"""
Example 3b:

This is essentially the same as example 3a, except we make our importer
into a function and use it to show how we technically should look for
a cached version of the module first
"""