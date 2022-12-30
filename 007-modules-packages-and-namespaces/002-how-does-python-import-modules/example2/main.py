# main.py
import module1

# even though test was added to sys.modules
# in module1, we can still access it from here
import test

print(f'{test()=}')

# Don't actually do this! It's a bad hack to illustrate how import
# looks in sys.modules for the symbol we are importing


