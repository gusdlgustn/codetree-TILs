n, k, T = map(str, input().split())
n = int(n); k = int(k)

str_arr = []
for i in range(n):
    str_arr.append(input())

sort_arr = []

for elem in str_arr:
    T_length = len(T)
    if elem[:T_length] == T:
        sort_arr.append(elem)

sort_arr.sort()
print(sort_arr[k-1])