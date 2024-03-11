A = input()


def is_different(string):
    first = string[0]
    for i in range(len(string)):
        if first != string[i]:
            return True
    return False

if is_different(A):
    print('Yes')
else:
    print('No')