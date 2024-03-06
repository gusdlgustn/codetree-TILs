n = int(input())

def is_magic_number(n):
    tens = n//10
    units = n%10
    if n%2 == 0 and (tens + units)%5 == 0:
        print('Yes')
    else:
        print('No')

is_magic_number(n)