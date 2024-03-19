N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

cnt = 1
for i in range(N-1):
    if (lst[i] == lst[i+1]):
        cnt += 1


print(cnt)