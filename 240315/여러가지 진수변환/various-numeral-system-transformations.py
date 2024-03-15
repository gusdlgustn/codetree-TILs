N, B = map(int, input().split())

changed = []
while True:
    if N < 2:
        changed.append(N)
        break
    
    changed.append(N%B)
    N //= B 

for elem in changed[::-1]:
    print(elem, end='')