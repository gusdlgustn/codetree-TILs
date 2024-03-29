n = int(input())

order = []
for i in range(n):
    x, direc = input().split()
    x = int(x)
    if direc == 'L':
        x = x*(-1)
    order.append(x)


sum_L = 0
sum_R = 0
for elem in order:
    if elem < 0:
        sum_L += elem*(-1)
    else:
        sum_R += elem


section = [0]*(sum_L + sum_R + 2) # 수평선 범위
current = 0 + sum_L # 0(시작위치) + offset

for moving in order:
    if moving > 0:
        for i in range(current, current+moving+1):
            section[i] += 1
    else: # moving < 0
        for i in range(current+moving, current+1):
            section[i] += 1
    current += moving

overlap = []
overlap_nonnested = []
tmp = []

for elem in section:
    if elem > 1:
        tmp.append(elem)
        overlap_nonnested.append(elem)
    else:
        overlap.append(tmp)
        tmp = []

overlap_final = []
for lst in overlap:
    if lst != []:
       overlap_final.append(lst)

print(len(overlap_nonnested)-len(overlap_final))