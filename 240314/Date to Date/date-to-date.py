m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_1 = 0
for i in range(1,m1+1):
    days_1 += num_of_days[i]
days_1 += d1

days_2 = 0
for i in range(1,m2+1):
    days_2 += num_of_days[i]
days_2 += d2

print(days_2 - days_1)