n = int(input())
int_arr = list(map(int, input().split()))

for i in range(n):
    if (i+1)%2 != 0:
        sub_arr = int_arr[:i+1]
        sub_arr.sort()
        print(sub_arr[i//2], end = ' ')