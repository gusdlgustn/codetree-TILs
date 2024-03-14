m1, d1, m2, d2 = map(int, input().split())

# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# days_1 = 0
# for i in range(1,m1+1):
#     days_1 += num_of_days[i]
# days_1 += d1

# days_2 = 0
# for i in range(1,m2+1):
#     days_2 += num_of_days[i]
# days_2 += d2

# if days_1 == days_2:
#     print(1)
# else:
#     print(days_2 - days_1)

month, day = m1, d1
elapsed_days = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if month == m2 and day == d2:
        break

    elapsed_days += 1
    day += 1

    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_days+1)