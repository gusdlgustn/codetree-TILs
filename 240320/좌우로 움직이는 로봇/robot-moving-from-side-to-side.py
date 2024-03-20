n, m = map(int, input().split())

A, B = [], []
for _ in range(n):
    t, d = input().split()
    t = int(t)
    A.append((t, d))

for _ in range(m):
    t, d = input().split()
    t = int(t)
    B.append((t, d))


A_loc, B_loc = [0], [0]
A_cur, B_cur = 0, 0

for t, d in A:
    if d == 'L':
        for _ in range(t):
            A_cur -= 1
            A_loc.append(A_cur)
    else: # d == 'R'
        for _ in range(t):
            A_cur += 1
            A_loc.append(A_cur)

for t, d in B:
    if d == 'L':
        for _ in range(t):
            B_cur -= 1
            B_loc.append(B_cur)
    else: # d == 'R'
        for _ in range(t):
            B_cur += 1
            B_loc.append(B_cur)

if len(A_loc) > len(B_loc):
    cur = B_loc[-1]
    for _ in range(len(A_loc)-len(B_loc)):
        B_loc.append(cur)
elif len(A_loc) < len(B_loc):
    cur = A_loc[-1]
    for _ in range(len(B_loc)-len(A_loc)):
        A_loc.append(cur)

length = len(A_loc)
cnt = 0

for i in range(1, length):
    if (A_loc[i-1] != B_loc[i-1]) and (A_loc[i] == B_loc[i]):
        cnt += 1

print(cnt)