N = int(input())
lst = list(map(int, input().split()))

arr = []
for i in range(N):
    arr.append((lst[i], i+11))
arr_sorted = arr[:]
arr_sorted.sort(key = lambda x:x[0])

idx = []
for i, e1 in enumerate(arr):
    for j, e2 in enumerate(arr_sorted):
        if e1 == e2:
            idx.append(j+1)

for e in idx:
    print(e, end = ' ')