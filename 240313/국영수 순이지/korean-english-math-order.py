n = int(input())

class Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

lst = []
for _ in range(n):
    name, kor, eng, math = input().split()
    lst.append(Grade(name, int(kor), int(eng), int(math)))

lst.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

for elem in lst:
    print(elem.name, elem.kor, elem.eng, elem.math)