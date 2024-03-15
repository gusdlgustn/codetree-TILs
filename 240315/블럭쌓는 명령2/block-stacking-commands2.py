N, K = map(int, input().split())

block = [0]*(N+1)

for i in range(K):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        block[j] += 1

maxx = max(block)
print(maxx)