N = int(input())

arr = [ # -1000부터 1000까지, 0은 안 주어짐
    int(input())
    for _ in range(N)
]

ans, cnt = 0, 0
for i in range(N):
    if (i >= 1) and ((arr[i-1] * arr[i]) > 0) :
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)