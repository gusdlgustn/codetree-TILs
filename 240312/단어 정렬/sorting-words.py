n = int(input())

str_arr = []
for i in range(n):
    str_arr.append(input())

str_arr.sort()

for elem in str_arr:
    print(elem)