# Good trick for emulating do-while loops
# PSEUDOCODE:
# do:
#    something()
# while:
#    CONDITION

def do_something():
    print('doing something')
    return True

# Note: the uncommented function below runs
# the do_something() function at least once no
# matter what and is more elegant than:
#
# result = do_something()
# while not result:
#     result = do_something()
#
# because it does not have to list the "result = do_something()"
# call twice

while True:
    result = do_something()
    if result:
        break

# while-else

breaking_condition = False
i = 0
while i < 10:
    i += 1
    if breaking_condition:
        print('while-loop break out early')
        break
else:
    print('while-loop completed. breaking condition never occurred.')

# while-else is useful for cases similar to the following:

# val = 10
# found = False
# idx = 0
# l = [1,2,3]

# while idx < len(l):
#     if l[idx] == val:
#         found = True
#         break
#     idx += 1

# if not found:
#     l.append(val)

val = 10
idx = 0
l = [1,2,3]
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
else:
    l.append(val)
print(l)

# of course, for this example, you would really just write:
l = [1,2,3]
if 10 not in l:
    l.append(10) 