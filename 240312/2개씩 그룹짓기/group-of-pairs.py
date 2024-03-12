N = int(input())
arr = list(map(int, input().split()))

arr.sort()
summ = 0

for i in range(N):
    maxx=0
    summ = arr[i]+arr[2*N-1-i]
    if summ>maxx:
        maxx = summ

print(maxx)