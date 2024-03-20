N, M, K = map(int, input().split())

students = [K for _ in range(0, N+1)] # 1~N번 학생 번호
students[0] = -1 # 0번 학생은 없다고 가정
penalty = [ # 벌칙 받는 학생의 번호
    int(input())
    for _ in range(M)
]

for p in penalty:
    students[p] -= 1
    if 0 in students:
        print(students.index(0))
        break

if not 0 in students:
    print(-1)