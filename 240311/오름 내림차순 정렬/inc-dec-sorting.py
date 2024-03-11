n = int(input())
arr = list(map(int, input().split()))

ascending  = sorted(arr)
descending  = sorted(arr, reverse=True)

for elem in ascending:
    print(elem, end=' ')
print()
for elem in descending:
    print(elem, end=' ')