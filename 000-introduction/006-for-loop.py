print('for-else example:')
# for-else example
for i in range(1,5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found!')
        break
else:
    print('no multiples of 7 were found')

print()
print('continue-finally example:')
# continue/finally example
for i in range(5):
    print('-'*20)
    try:
        10 / (i-3)
        print(f'TRY 10 / {i - 3} -- try')
    except ZeroDivisionError:
        print('EXCEPT attempted to divide by zero')
        continue
    finally:
        print('FINALLY always runs, even on errors')
    print(f'POST-TRY-BLOCK loop does not run after continue-finally')