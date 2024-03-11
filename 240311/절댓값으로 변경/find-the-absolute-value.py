N = int(input())
arr = list(map(int, input().split()))

def absolute(arr):
    for i in range(N):
        if arr[i] < 0:
            arr[i] = -arr[i]

absolute(arr)

for elem in arr:
    print(elem, end=' ')