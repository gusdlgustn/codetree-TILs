n = int(input())

class Grade:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

lst = []
for _ in range(n):
    name, sub1, sub2, sub3 = input().split()
    lst.append(Grade(name, int(sub1), int(sub2), int(sub3)))

lst.sort(key = lambda x: x.sub1 + x.sub2 + x.sub3)

for elem in lst:
    print(elem.name, elem.sub1, elem.sub2, elem.sub3)