import ctypes

# =======================================

print('Simple int memory address examples:')

print('\n(1.)')
a = 10
print('\na = 10')
print(f'{hex(id(a))=}')
print(f'{hex(id(10))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(2.)')

a = 10
print('\na = 10')
b = a
print('b = a')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(3.)')

a = 10
print('\na = 10')
b = a
print('b = a')
b = 10
print('b = 10')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(4.)')

a = 10
print('\na = 10')
b = a
print('b = a')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')

b = 11
print('b = 11')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')

print(f'{hex(id(10))=}')
print(f'{hex(id(11))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+  {hex(id(11))}  +       11         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(5.)')

a = 10
print('\na = 10')
b = 10
print('b = 10')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')

a = 11
print('a = 11')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')
print(f'{hex(id(11))=}')

b = 11
print('b = 11')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')
print(f'{hex(id(11))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+  {hex(id(11))}  +       11         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(6.)')

b = 12
print('\nb = 12')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')
print(f'{hex(id(11))=}')
print(f'{hex(id(12))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+  {hex(id(11))}  +       11         +
+  {hex(id(12))}  +       12         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(7.)')

a = 10
b = a
a = 11
print('\na = 10')
print('b = a')
print('a = 11')
print(f'{hex(id(a))=}')
print(f'{hex(id(b))=}')
print(f'{hex(id(10))=}')
print(f'{hex(id(11))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id(10))}  +       10         +
+  {hex(id(11))}  +       11         +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+         a        +  {hex(id(a))}  +
+         b        +  {hex(id(b))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\nSimple string memory address examples:')

print('\n(8.)')

greeting = 'hello'
print("\ngreeting = 'hello'")
print(f'{hex(id(greeting))=}')
print(f'{hex(id("hello"))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id('hello'))}  +     'hello'      +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+     greeting     +  {hex(id(greeting))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

# =======================================

print('\n(9.)')

greeting = 'hello'
print("\ngreeting = 'hello'")
print(f'{hex(id(greeting))=}')
print(f'{hex(id("hello"))=}')

greeting += ' world'
print("\ngreeting += ' world'")
print(f'{hex(id(greeting))=}')
print(f'{hex(id("hello"))=}')
print(f'{hex(id("hello world"))=}')



heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id('hello'))}  +     'hello'      +
+  {hex(id('hello world'))}  +  'hello world'   +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+     greeting     +  {hex(id(greeting))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

print(f'{ctypes.cast(id(greeting), ctypes.py_object).value=}')

greeting = 'hello world'
print("\ngreeting = 'hello world'")

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id('hello world'))}  +  'hello world'   +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+     greeting     +  {hex(id(greeting))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)


# =======================================
print('\nSimple list memory address examples:')

print('\n(10.)')

list_1 = [1,2,3]
print("\nlist_1 = [1,2,3]")
print(f'{hex(id(list_1))=}')
print(f'{hex(id([1,2,3]))=}')
print("\nlist_2 = list_1")

list_2 = list_1

note = """
Note: one potentially confusing point. Once [1,2,3]
gets declared with hex(id([1,2,3])), list_3 latches
onto it and hex(id([1,2,3])) CHANGES!! to another
area of memory
"""

print(note)
print(f'{hex(id([1,2,3]))=}')
print("list_3 = [1,2,3]")
list_3 = [1,2,3]
print(f'{hex(id(list_3))=}')
print(f'{hex(id([1,2,3]))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id([1,2,3]))}  +     [1,2,3]      +
+  {hex(id(list_1))}  +     [1,2,3]      +
+  {hex(id(list_3))}  +     [1,2,3]      +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+      list_1      +  {hex(id(list_1))}  +
+      list_2      +  {hex(id(list_2))}  +
+      list_3      +  {hex(id(list_3))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)

print('\nlist_1.append(4)')
list_1.append(4)

print(f'{hex(id([1,2,3]))=}')
print(f'{hex(id([1,2,3,4]))=}')
print(f'{hex(id(list_1))=}')
print(f'{hex(id(list_2))=}')
print(f'{hex(id(list_3))=}')
print(f'{list_1=}')
print(f'{list_2=}')
print(f'{list_3=}')

print('\nlist_3.append(4)')
list_3.append(4)
print(f'{hex(id(list_1))=}')
print(f'{hex(id(list_2))=}')
print(f'{hex(id(list_3))=}')

heap = f"""
Heap:
+++++++++++++++++++++++++++++++++++++++
+     Address      +      Value       +
+++++++++++++++++++++++++++++++++++++++
+  {hex(id([1,2,3]))}  +     [1,2,3]      +
+  {hex(id(list_1))}  +    [1,2,3,4]     +
+  {hex(id(list_3))}  +    [1,2,3,4]     +
+++++++++++++++++++++++++++++++++++++++
"""

refs = f"""Refs:
+++++++++++++++++++++++++++++++++++++++
+       Var        +      Value       +
+++++++++++++++++++++++++++++++++++++++
+      list_1      +  {hex(id(list_1))}  +
+      list_2      +  {hex(id(list_2))}  +
+      list_3      +  {hex(id(list_3))}  +
+++++++++++++++++++++++++++++++++++++++
"""

print(heap)
print(refs)