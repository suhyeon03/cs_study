n = int(input())

name = []
score1 = []
score2 = []
score3 = []

for _ in range(n):
    student_input = input().split()
    name.append(student_input[0])
    score1.append(int(student_input[1]))
    score2.append(int(student_input[2]))
    score3.append(int(student_input[3]))

# Please write your code here.

class student:
    def __init__(self,name ,score_1, score_2, score_3):
        self.n = name
        self.a = score_1
        self.b = score_2
        self.c = score_3

student_score = []

for i in range(n):
    student_score.append(student(name[i], score1[i], score2[i], score3[i]))

student_score.sort(key=lambda x: x.a + x.b + x.c)
for student in student_score:
    print(student.n, student.a, student.b, student.c)