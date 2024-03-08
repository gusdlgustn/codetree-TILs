M, D = map(int, input().split())

# def is_month(n):
#     if n <= 12:
#         return True
#     else:
#         return False

def is_day(m, n):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        if n <= 31:
            return True
    elif m==4 or m==6 or m==9 or m==11:
        if n <= 30:
            return True
    elif m==2:
        if n <= 28:
            return True
    else:
        return False

if is_day(M, D):
    print('Yes')
else:
    print('No')