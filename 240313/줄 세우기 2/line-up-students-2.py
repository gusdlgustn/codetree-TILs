N = int(input())

class Student:
    def __init__(self, height, weight, num):
        self.h = height
        self.w = weight
        self.num = num

lst = []
for i in range(N):
    h, w = map(int, input().split())
    lst.append(Student(h, w, i+1))


lst.sort(key=lambda x:(x.h, -x.w))

for e in lst:
    print(e.h, e.w, e.num)