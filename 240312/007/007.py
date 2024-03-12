code, point, time = input().split()

class Class007:
    def __init__(self, c, p, t):
        self.code = c
        self.point = p
        self.time = t

output = Class007(code, point, time)

print("secret code :", output.code)
print("meeting point :", output.point)
print("time :", output.time)