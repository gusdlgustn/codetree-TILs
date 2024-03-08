n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def is_subseq(A, B, n1, n2):
    for i in range(n1-n2):
        sub_A = A[0+i:n2+i]
        if sub_A == B:
            return True
    return False

if is_subseq(A, B, n1, n2):
    print('Yes')
else:
    print('No')