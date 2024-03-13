code, color, second = input().split()

class Clear:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

a = Clear(code, color, second)

print("code :", a.code)
print("color :", a.color)
print("second :", a.sec)