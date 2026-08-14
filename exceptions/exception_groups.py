# when dealing with concurrent programs, multiple errors can arise 
# we want a way of handling each of these errors (either at once or)
# separately, and we can through this through exception groups

try:
    raise ExceptionGroup('group', [
        ValueError('aaa'), 
        ZeroDivisionError('bbb'),
        NameError('ccc')
    ])

except* ValueError as eg:
    print('handling value error: ', eg.exceptions)

except* (ZeroDivisionError, NameError) as eg:
    print('handling some error: ', eg.exceptions)


# handling value error:  (ValueError('aaa'),)
# handling some error:  (ZeroDivisionError('bbb'), NameError('ccc'))