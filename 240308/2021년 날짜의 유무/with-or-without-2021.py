M, D = map(int, input().split())

# def is_month(n):
#     if n <= 12:
#         return True
#     else:
#         return False

def is_day(m, n):
    if m==1 or 3 or 5 or 7 or 8 or 10 or 12:
        if n <= 31:
            return True
    elif m==4 or 6 or 9 or 11:
        if n <= 30:
            return True
    elif m==2:
        if n <= 28:
            return True
    return False

if is_day(M, D):
    print('Yes')
else:
    print('No')