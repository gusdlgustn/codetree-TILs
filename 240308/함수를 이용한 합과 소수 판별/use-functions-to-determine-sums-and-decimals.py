a, b = map(int, input().split())

def is_prime(n):
    if n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def is_even(n):
    hundreds = n//100
    tens = n//10
    ones = (n - hundreds*100 - tens*10)
    if (hundreds + tens + ones)%2 == 0:
        return True
    else:
        return False 

result = 0
for i in range(a, b+1):
    if is_prime(i) and is_even(i):
        result += 1

print(result)