N, M = map(int, input().split())

A = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

B = [
    tuple(map(int, input().split()))
    for _ in range(M)
]

A_loc, B_loc = [0], [0] # 인덱스 = 시간
A_cur, B_cur = 0, 0

for v, t in A:
    for time in range(t):
        A_loc.append(A_cur + v)
        A_cur = A_loc[-1]

for v, t in B:
    for time in range(t):
        B_loc.append(B_cur + v)
        B_cur = B_loc[-1]

cnt = 0
total_t = len(A_loc)
head = []
for i in range(1, total_t):
    if A_loc[i] > B_loc[i]:
        head.append('A')
    elif A_loc[i] < B_loc[i]:
        head.append('B')
    else: # A_loc[i] == B_loc[i]
        pass

# 바뀌면 count 추가
cnt = 0
for i in range(len(head)):
    if (i >= 1) and (head[i-1] != head[i]):
        cnt += 1
print(cnt)