N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

ans, cnt = 0, 1
for i in range(N-1):
    if i >= 1 and (lst[i] == lst[i+1]):
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)
print(ans)