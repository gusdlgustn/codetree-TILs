n = int(input())

def devide(n):
    summ = 0
    for i in range(0, n+1):
        summ += i
    
    result = summ/10
    result = int(result)
    return result

a = devide(n)
print(a)