"""
Decorator Application: Single Dispatch Generic Functions
"""

from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

def html_real(a):
    return f'{round(a, 2):.2f}'

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = (f'<li>{html_escape(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(html_str("""This is 
a multi-line string with special characters: 10 < 100"""))
print(html_int(255))
print(html_escape(3+10j))

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)


ml_string = """Python
rocks!
"""
print(f'{htmlize(100)=}')
print(f'{htmlize(ml_string)=}')
print(f'{htmlize([1,2,3])=}')
print()
print('Note no <br>, NOT as desired')
print(htmlize(["""Python
rocks! 0 < 1
""",(10,20,30), 100]))

def func1():
    func2()

def func2():
    print("not a true circular reference")

func1()

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set):
        return html_set(arg)
    else:
        return html_escape(arg)

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'

def html_real(a):
    return f'{round(a, 2):.2f}'

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = (f'<li>{htmlize(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = (f'<li>{html_escape(k)}={htmlize(v)}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print()
print(htmlize(["""Python
rocks! 0 < 1
""",(10,20,30), 100]))

""" But what if we want to add a new type? """

def html_set(arg):
    return html_list(arg)

print()
print(htmlize({"a", "b", "c"}))

""" The issue is that whenever we add a new type, we have to add to this
ugly if/elif chain. """

def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        dict: html_dict,
        set: html_set
    }
    fn = registry.get(type(arg), registry[object])
    return fn(arg)

print()
print(f'{htmlize(100)=}')
print(f'{htmlize([1,2,3])=}')

""" But again, whenever we add a new type, we have to modify the dictionary registry in the function """

