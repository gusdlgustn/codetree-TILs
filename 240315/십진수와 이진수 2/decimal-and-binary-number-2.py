N = list(map(int, list(input())))


# 10진수로 바꾸기
decimal = 0
for i in range(len(N)):
    decimal = decimal*2 + N[i]

decimal *= 17

# 2진수로 바꾸기
binary = []
while True:
    if decimal<2:
        binary.append(decimal)
        break
    
    binary.append(decimal%2)
    decimal //= 2

for i in binary[::-1]:
    print(i, end='')