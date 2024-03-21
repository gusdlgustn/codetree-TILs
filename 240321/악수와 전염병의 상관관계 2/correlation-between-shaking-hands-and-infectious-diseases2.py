N, K, P, T = map(int, input().split())
# 개발자 N명
# 개발자가 감염되면 최대 K번 이내의 악수에 대해서만 전염병 옮김
# 초기 감염자의 번호 P
# 악수 횟수 T번
handshake = [
    tuple(map(int, input().split())) # (t, x, y) t초에 x와 y가 악수함
    for _ in range(T)
]

num = [-1]*(N+1) # n번 인덱스 = n번 개발자, 감염 여부 겸 몇 번 악수해서 전염시켰는지 기록
num[P] = 0 # 이미 감염된 사람
# 한 번 악수할 때마다 num += 1, P번 초과해서 악수하면 악수 기록 x
handshake.sort(key=lambda x: x[0]) # t를 기준으로 오름차순 정렬


for _, x, y in handshake:
    if num[x] < 0 and num[y] < 0: # 둘 다 비감염자
        pass

    elif num[x] >= 0 and num[y] < 0: # x:감염자, y:비감염자
        if num[x] >= P: # P번 초과해서 악수했을 경우 pass
            pass
        else:
            num[x] += 1
            num[y] += 1

    elif num[x] < 0 and num[y] >= 0: # x:비감염자, y:감염자
        if num[y] >= P:
            pass
        else:
            num[x] += 1
            num[y] += 1

    else: # 둘 다 감염자
        if num[x] >= P and num[y] >= P:
            pass
        elif num[x] >= P:
            num[y] += 1
        elif num[y] >= P:
            num[x] += 1
        else:
            num[x] +=1
            num[y] += 1

for i in range(1, len(num)):
    if num[i] < 0: #비감염자
        print(0, end = '')
    else:
        print(1, end = '')