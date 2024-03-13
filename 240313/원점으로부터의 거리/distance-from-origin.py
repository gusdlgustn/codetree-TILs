N = int(input())

class Point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

lst = []
for i in range(N):
    x, y = map(int, input().split())
    lst.append(Point(x, y, i+1))

lst.sort(key=lambda x:(abs(x.x)+abs(x.y), x.num))

for e in lst:
    print(e.num)