N = int(input())

lst = []
for i in range(N):
    h, w = map(int, input().split())
    lst.append((h, w, i+1)) # 키, 몸무게, 번호

lst.sort(key=lambda x:(-x[0], -x[1], x[2]))

for elem in lst:
    print(elem[0], elem[1], elem[2])