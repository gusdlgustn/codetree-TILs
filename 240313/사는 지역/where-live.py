n = int(input())

class Region:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self. city = city


lst = []
for _ in range(n):
    name, address, city = input().split()
    lst.append(Region(name, address, city))

max_idx = 0

for i in range(n):
    if lst[i].name > lst[max_idx].name:
        max_idx = i

print('name', lst[max_idx].name)
print('addr', lst[max_idx].address)
print('city', lst[max_idx].city)