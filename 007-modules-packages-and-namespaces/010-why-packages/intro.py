"""
Why packages?

Code Organization, Ease of Use...

Suppose you have 50 different functions and classes in your program

Approach #1: Put them all in one file

# api.py                          (single file)
-----------------------------------------------
===========
<functions>
===========
connect
execute_no_result
execute_single_row
execute_multi_row

normalize_string
convert_str_to_bool
format_iso_date
current_time_utc

authenticate
validate_token
get_permissions
authorize_endpoint

=========
<classes>
=========
User
UserProfile
Users

BlogPost
BlogPosts

RouteTable
Configuration

JSONEncoder

UnitTests

=======
<other>
=======
audit_endpoint

Logger

validate_email
validate_phone
validate_name

etc...

In one file???

Would be very difficult to understand what is going on in the file
"""

"""
Approach #2: Start with Modules...

api/
    api.py
    dbutilities.py
    jsonutilities.py
    typeconversions.py
    validations.py
    authentication.py
    authorization.py
    users.py
    blogposts.py
    logging.py
    unittests.py

Better... a bit more organized

But still unwieldy - everything is at the top level

Too many imports:
    import dbutilities
    import jsonutilities
    import typeconversions
    import validations
    import authentication
    import authorization
    import users
    ...

Certain modules could be broken down further:

dbutilities -> connections, queries
users -> User, Users, UserProfile

Certain modules belong "together":

authentication, authorization -> security
"""

"""
Approach #3: Packages!

api/
|---- utilities/
|     |     __init__.py
|     |---- database/
|     |     |     __init__.py
|     |     |     connections.py
|     |     |     queries.py
|     |---- json/
|     |     |     __init__.py
|     |     |     encoders.py
|     |     |     decoders.py
|---- security/
|     |     __init__.py
|     |     authentication.py
|     |     authorization.py
|---- models/
|     |     __init__.py
|     |---- users.py
|     |     |     __init__.py
|     |     |     user.py
|     |     |     userprofile.py

This allows us to give structure to our code
    - It's now much easier to navigate
    - Also we're starting to break things down into smaller code files.
      We don't want large code files. The larger the file is, the more
      difficult it is to understand. So we want to try to break things
      down into smaller components. Just like we don't write functions
      with thousands of lines of code.
"""

"""
Another Use Case

You have a module that implements 2 functions/classes for users of the
module.
These two objects require 20 different helper functions and 2 additional
helper classes.

From *module developer's* perspective:
    - Much easier to break the code down into multiple modules

From *module user's* perspective:
    - They just want a single import for the function and class
"""

"""
Module Developer's Perspective

mylib/
    __init__.py
    submod1.py         <-- function to be exported to user lives here
    submod2.py
    subpack1
        __init__.py
        pack1mod1.py
        pack1mod2.py   <-- class to be exported to user lives here

Smaller code modules, with a specific purpose, are easier to write, debug,
test, and understand
"""

"""
Module User's Perspective

User should not have to write:
from mylib.submod1 import my_func
from mylib.subpack1.pack1mod2 import MyClass

They are seeing the internal implementation details of the package,
which is not user-friendly.

Much easier for user if they could write:

from mylib import my_func, MyClass

OR, simply:

import mylib
mylib.my_func()
mylib.MyClass()
"""

"""
Using __init__.py

We can use packages' __init__.py code to **export** (expose) just what's needed by our users
"""

"""
Example:

mylib/
    __init__.py
    submod1.py         <-- function to be exported to user lives here
    submod2.py
    subpack1
        __init__.py
        pack1mod1.py
        pack1mod2.py   <-- class to be exported to user lives here

# __init__.py
from mylib.submod1 import my_func
from mylib.subpack1.pack1mod2 import MyClass

User uses it this way:
import mylib

mylib.my_func()
mylib.MyClass()

Our internal implementation is "hidden"

We'll cover this in the next video
"""

"""
Recap: Why packages?
- ability to break code up into smaller chunks makes our code:
    - easier to write
    - easier to test and debug
    - easier to read/understand
    - easier to document

Just like books are divided into chapters, sections, paragraphs, sentences, etc.

But they can still be "stitched" together
    - hides inner implementation from users
    - makes their code
        - easier to write
        - easier to test and debug
        - easier to read/understand
"""