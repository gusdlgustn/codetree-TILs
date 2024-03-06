def game(n):
    n = str(n)
    result = [i for i in n]
    true = False
    for i in result:
        if i == '3' or i =='6' or i =='9':
            true = True
    return true

def three(n):
    return n%3==0

a, b = map(int, input().split())

count = 0
for i in range(a, b+1):
    if game(i) or three(i):
        count += 1
print(count)