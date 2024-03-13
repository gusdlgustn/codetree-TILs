class Student:
    def __init__(self, id, score):
        self.id = id
        self.score = score

students = []
for _ in range(5):
    id, score = input().split()
    score = int(score)
    students.append(Student(id, score))

min = 100
for i in range(5):
    agent_score = students[i].score
    if agent_score < min:
        min = agent_score
        idx = i

print(students[idx].id, students[idx].score)