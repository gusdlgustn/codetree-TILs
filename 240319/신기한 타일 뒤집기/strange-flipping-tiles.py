n = int(input())

move = []

for _ in range(n):
    distance, direction = input().split()
    distance = int(distance)
    move.append((distance, direction))

offset = 100000 # 100 * 1000

current = 100000 # 현재 위치(0) + offset

tile = [[''] for _ in range(200001)]

for distance, direction in move:
    if direction == 'L': # 흰색
        for i in range(current-distance+1, current+1):
            tile[i] += ['W'] # 흰색 추가
        current -= (distance-1)
    else: # direction == 'R' 검은색
        for i in range(current, current+distance):
            tile[i] += ['B'] # 흰색 추가
        current += (distance-1)

W = 0 # 흰색
B = 0 # 검은색
G = 0 # 회색

for elem in tile:
    if elem[-1] == 'W':
        W += 1
    elif elem[-1] == 'B':
        B += 1

print(W, B)