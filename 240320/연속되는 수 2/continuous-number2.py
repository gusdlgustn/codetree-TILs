N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

ans, cnt = 0, 0
for i in range(N):
	# Case 1
	if i >= 1 and lst[i] == lst[i - 1]:
		cnt += 1
	# Case 2
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)