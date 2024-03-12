N, k = map(int, input().split())
int_arr = list(map(int, input().split()))

int_arr.sort()
print(int_arr[k-1])