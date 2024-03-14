m1, d1, m2, d2 = map(int, input().split())
# m1, d1, m2, d2 = 3, 4, 4, 3

A = input() # 요일

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day1 = 0
for i in range(m1):
    day1 += num_of_days[i]
day1 += d1

day2 = 0
for i in range(m2):
    day2 += num_of_days[i]
day2 += d2

diff = day2 - day1
quotient = diff // 7
remainder = diff % 7

count = [quotient]*7
for i in range(remainder+1):
    count[i] += 1

idx = days.index(A)
print(count[idx])