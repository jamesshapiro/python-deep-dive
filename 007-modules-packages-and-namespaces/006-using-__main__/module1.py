# module1.py

print(f'loading module1.py: __name__ = {__name__}')

"""
Running:

> python3 module1.py # yields:
$ loading module1.py: __name__ = __main__
"""

if __name__ == '__main__':
    print(f'Module was executed as a script...')