"""
Import variants
"""

# module1.py
import math

"""
What is this doing? ^^

1.) Check if math is in sys.modules
2.) If not, load it and insert ref into sys.modules

sys.modules
+-----------------+-----------------+
| math            | <module object> |
+-----------------+-----------------+

3.) Add symbol "math" to module1's global namespace referencing the same object

module1.globals()
+-----------------+-----------------+
| math            | <module object> |
+-----------------+-----------------+

(If "math" symbol already exists in module1's global namespace, it will be overwritten)
"""

# second example:
import math as r_math
"""
What is this doing? ^^

1.) Check if math is in sys.modules
2.) If not, load it and insert ref into sys.modules

sys.modules
+-----------------+--------------------+
| math            | <module object>    |
+-----------------+--------------------+

3.) Add symbol "r_math" to module1's global namespace referencing the same object

module1.globals()
+-----------------+--------------------+
| math            | <module object>    |
+-----------------+--------------------+

Note: "r_math" symbol is now in our namespace, however "math" symbol is not

(If "r_math" symbol already exists in module1's global namespace, it will be overwritten)
"""

# third example:
from math import sqrt
"""
What is this doing? ^^

1.) Check if math is in sys.modules
2.) If not, load it and insert ref into sys.modules

sys.modules
+-----------------+--------------------+
| math            | <module object>    |
+-----------------+--------------------+

3.) Add symbol "sqrt" to module1's global namespace referencing the the function math.sqrt

module1.globals()
+-----------------+--------------------+
| sqrt            | <math.sqrt object> |
+-----------------+--------------------+

Note: "sqrt" symbol is now in our namespace, however "math" symbol is not

(If "sqrt" symbol already exists in module1's global namespace, it will be overwritten)

Note that the math module is still loaded! It's in sys.modules, it's just unavailable
in our namespace. SEE: import_variant_experiment.py
"""

# fourth example:
# third example:
from math import *
"""
What is this doing? ^^

1.) Check if math is in sys.modules
2.) If not, load it and insert ref into sys.modules

sys.modules
+-----------------+--------------------+
| math            | <module object>    |
+-----------------+--------------------+

3.) Add "all" symbols defined in math to module1's global namespace
- But note: what "all" means can be defined by the module being imported

module1.globals()
+-----------------+--------------------+
| sqrt            | <math.sqrt object> |
| pi              | <math.pi object>   |
| sin             | <math.sin object>  |
| e               | <math.e object>    |
+-----------------+--------------------+

Note: these symbols are now in our namespace, however "math" symbol is not

(If any symbols already exist in module1's global namespace, replace their reference)
"""


"""
BIG TAKEAWAY:

Running "from math import sqrt"

Does not "partially" load math. It's not more efficient than "import math"

Math is loaded into memory in both cases.
"""

"""
However, also note:

Things may be different with packages, but for simple modules, this is the behavior
"""

"""
Why "from <module> import <symbol>" can lead to bugs:

"""

#module1.py
from cmath import *

"""
module1.globals()
+-----------------+--------------------+
| sqrt            | <cmath.sqrt>       |
| ...             | ...                |
+-----------------+--------------------+
"""

from math import *
"""
module1.globals()
+-----------------+--------------------+
| sqrt            | <math.sqrt>        |
| ...             | ...                |
+-----------------+--------------------+
"""

"""
These two imports step on each other's toes and can lead to bugs

So that is why import * is disfavored
"""

"""
Efficiency

What's more efficient:
- import math
- from math import sqrt

importing -> same amount of work

calling
-> math.sqrt(2) [This first needs to find the sqrt symbol in math's namespace]
-> sqrt(2)

However, dict lookups are super fast! So generally this will be negligible

Additionally, math.sqrt(2) is more readable. You know where the function is coming from
So generally, don't write sqrt(2) for optimization reasons unless it's absolutely necessary
"""

# CODING SECTION #

"""
Let's see what we get out of the box:
"""
import sys
print(f'\n{sys.modules.keys()}')

from cmath import sin as c_sin
from math import sin as r_sin

