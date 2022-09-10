# try ... except ... finally
a = 10
b = 1
print('finally, basic example -- non-error case:')
try:
    a/b
except ZeroDivisionError:
    print('EXCEPT division by zero error caught')
finally:
    print('FINALLY this always executes')

print('\nfinally, basic example -- error case:')
a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('EXCEPT division by zero error caught')
finally:
    print('FINALLY this always executes')
print()

print('continue-finally example:')
# finally example with continue
a = 0
b = 2
while a < 4:
    print('-'*20)
    a += 1
    b -= 1
    try:
        a / b
    except ZeroDivisionError:
        print(f'EXCEPT {a}/{b} division by zero error caught - loop')
        continue
    # NOTE: this will execute even with a continue statement!!!
    # This is great, it lets you close a file, or a DB connection
    # rollback a transaction, etc.
    finally:
        print(f'FINALLY {a}/{b} this always executes - loop')
    print(f'POST-TRY-BLOCK {a}/{b} - main loop')

print('\nbreak-finally example:')
# finally example with break
a = 0
b = 2
while a < 4:
    print('-'*20)
    a += 1
    b -= 1
    try:
        a / b
    except ZeroDivisionError:
        print(f'EXCEPT {a}/{b} division by zero - loop')
        break
    # NOTE: this will execute even with a continue statement!!!
    # This is great, it lets you close a file, or a DB connection
    # rollback a transaction, etc.
    finally:
        print(f'FINALLY {a}/{b} this always executes - loop')
    print(f'POST-TRY-BLOCK {a}/{b} - main loop')

