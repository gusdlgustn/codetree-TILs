N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

cnt = 0
for i in range(N):
    if (i == 0) or (lst[i] == lst[i - 1]):
        cnt += 1

print(cnt)