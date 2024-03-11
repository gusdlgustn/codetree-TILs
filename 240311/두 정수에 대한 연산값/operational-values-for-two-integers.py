a, b = map(int, input().split())

def cal(a, b):
    if a<b:
        a *= 2
        b += 25
    else:
        b *= 2
        a += 25
    return a, b

a, b = cal(a, b)
print(a, b)