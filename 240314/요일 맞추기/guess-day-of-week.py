m1, d1, m2, d2 = map(int, input().split())

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = 0
for i in range(m1):
    day1 += num_of_days[i]
day1 += d1

day2 = 0
for i in range(m2):
    day2 += num_of_days[i]
day2 += d2

diff = day2-day1


remainder = diff%7
print(days[remainder])