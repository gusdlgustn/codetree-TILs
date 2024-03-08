a, o, c = map(str, input().split())
a = int(a); c = int(c)

def add(a, c):
    return a+c

def multiple(a, c):
    return a*c

def minus(a, c):
    return a-c

def devide(a, c):
    return a//c

if o == '+':
    print(f"{a} {o} {c} = {add(a, c)}")
elif o == '*':
    print(f"{a} {o} {c} = {multiple(a, c)}")
elif o == '-':
    print(f"{a} {o} {c} = {minus(a, c)}")
elif o == '/':
    print(f"{a} {o} {c} = {devide(a, c)}")
else:
    print("False")