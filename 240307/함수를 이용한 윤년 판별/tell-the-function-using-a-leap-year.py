y = int(input())

def leap_year(n):
    if n%4 == 0:
        if n%100==0 and n%400!=0:
            return False
        return True
    return False

if leap_year(y):
    print('true')
else:
    print('false')