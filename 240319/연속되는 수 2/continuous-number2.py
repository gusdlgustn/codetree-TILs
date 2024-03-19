N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

ans, cnt = 0, 1
for i in range(1, N-1):
    if (lst[i] == lst[i+1]):
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)
print(ans)