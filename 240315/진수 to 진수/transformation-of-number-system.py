a, b = map(int, input().split())
n = input()

# a진수 -> 10진수
decimal = 0
for i in range(len(n)):
    decimal = decimal*a + int(n[i])

# 10진수 -> b진수
new = []
while True:
    if decimal<b:
        new.append(decimal)
        break
    new.append(decimal%b)
    decimal //= b 

for i in new[::-1]:
    print(i, end='')