# validators

# import common.validators.boolean
# import common.validators.date
# import common.validators.json
# import common.validators.numeric

"""
So this is one case where you might actually want to use import *
"""

from .boolean import *
from .date import *
from .json import *
from .numeric import *

__all__ = ['is_boolean', 'is_json']

# Alternatively can do something like:

"""
__all__ = (
    boolean.__all__ +
    date.__all__ +
    json.__all__ +
    numeric.__all__
)
"""