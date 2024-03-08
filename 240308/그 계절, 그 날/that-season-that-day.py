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
    elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d<=31):
        if (m==1 or m==12):
            print('Winter')
        elif m==3 or m==5:
            print('Spring')
        elif m==7 or m==8:
            print('Summer')
        else:
            print('Fall')
    else: print(-1)

is_day(Y, M, D)