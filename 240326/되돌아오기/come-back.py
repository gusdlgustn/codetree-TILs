N = int(input())
arr = []
for _ in range(N):
    direc, dist = input().split()
    dist = int(dist)
    arr.append((direc, dist))

x, y = 0, 0
move_dir = 0
    #  동 남 서 북
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

mapper = {
    'E':0,
    'S':1,
    'W':2,
    'N':3
}
comeback = False
time = 0
for direc, dist in arr:
    move_dir = mapper[direc]
    for _ in range(dist):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        x, y = nx, ny
        time += 1

        if x == 0 and y == 0:
            print(time)
            comeback = True
            break
        

if not comeback:
    print(-1)