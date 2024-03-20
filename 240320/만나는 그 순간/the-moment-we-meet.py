N, M = map(int, input().split())

A, B = [], []
for _ in range(N):
    d, t = input().split()
    t = int(t)
    A.append((d, t))

for _ in range(M):
    d, t = input().split()
    t = int(t)
    B.append((d, t))


# A 위치
A_loc = [0]
A_cur = 0
for d, t in A:
    if d == 'L':
        for i in range(t):
            A_cur -= 1
            A_loc.append(A_cur)
    elif d == 'R':
        for i in range(t):
            A_cur += 1
            A_loc.append(A_cur)

# B 위치
B_loc = [0]
B_cur = 0
for d, t in B:
    if d == 'L':
        for i in range(t):
            B_cur -= 1
            B_loc.append(B_cur)
    elif d == 'R':
        for i in range(t):
            B_cur += 1
            B_loc.append(B_cur)


for i in range(max(len(A_loc), len(B_loc))):
    if i == 0:
        pass
    elif A_loc[i] == B_loc[i]:
        print(i)
        break
    else:
        print(-1)