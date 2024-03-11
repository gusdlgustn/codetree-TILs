N = int(input())
arr = list(map(int, input().split()))

def devide(arr):
    for i in range(N):
        if arr[i]%2 == 0:
            arr[i] /= 2
            arr[i] = int(arr[i])

devide(arr)

for elem in arr:
    print(elem, end=' ')