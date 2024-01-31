# opening file/resource

try:
    # logic to read
    i = 0   # getting input from user
    j = 10 / i
    values = [1, '1']
    sum(values)
except TypeError:
    print('TypeError')
    j=0
except ZeroDivisionError:
    print('ZeroDivisionError')
    j=0
except:
    print('OtherError')
else:       # else is executed if exception is not thrown
    print('Else')
finally:
    # close file
    print('Finally')


print(j)
print('End')