a, b = map(int, input().split())
lst = [] # 소수 담을 리스트

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    
    return True


for i in range(a, b+1):
    if is_prime(i):
        lst.append(i)

print(sum(lst))