A = input() # 문자열

def reverse(string):
    return string[::-1]

if A == reverse(A):
    print('Yes')
else:
    print('No')