n, t = map(int, input().split())

arr = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(n):
    if (i >= 1) and ((t < arr[i-1]) and (t < arr[i])):
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)


if cnt == 1:
    print(0)
else:
    print(ans)