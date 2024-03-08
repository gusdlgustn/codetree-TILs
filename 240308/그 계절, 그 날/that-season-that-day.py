Y, M, D = tuple(map(int, input().split()))

def is_leapyear(n):
    if (n%4 == 0):
        if n%100==0 and n%400==0:
            return True
        if n%100 == 0:
            return False
        else:
            return True
    return False

def is_day(y, m, d):
    if (m==4 or m==6 or m==9 or m==11) and (d<=30):
        if m==4:
            print('Spring')
        elif m==6:
            print('Summer')
        else:
            print('Fall')
    elif m==2:
        if is_leapyear(y):
            if d<=29:
                print('Winter')
            else:
                print(-1)
        else:
            if d<=28:
                print('Winter')
            else:
                print(-1)
    else:
        print(-1)

is_day(Y, M, D)