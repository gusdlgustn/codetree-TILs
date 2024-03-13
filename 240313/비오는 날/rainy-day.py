n = int(input())

class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

lst = []
for _ in range(n):
    date, day, weather = input().split()
    lst.append(Data(date, day, weather))

lst_rain = []
for i in range(n):
    if lst[i].weather == 'Rain':
        lst_rain.append(lst[i])

del lst

recent = '2100-12-31'
for i in range(len(lst_rain)):
    if lst_rain[i].date <= recent:
        recent = lst_rain[i].date
        recent_data = lst_rain[i]

print(recent_data.date, recent_data.day, recent_data.weather)