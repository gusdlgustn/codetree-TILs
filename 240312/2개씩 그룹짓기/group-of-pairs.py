N = int(input())
arr = list(map(int, input().split()))

arr.sort()

maxx=0
for i in range(N):
    summ = arr[i]+arr[2*N-1-i]
    if summ>maxx:
        maxx = summ

print(maxx)