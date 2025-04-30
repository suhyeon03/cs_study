n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class student:
    def __init__(self, name='', korean=0, english=0, math=0):
        self.n = name
        self.k = korean
        self.e = english
        self.m = math

student_score = []
for i in range (n):
    student_score.append(student(name[i],korean[i],english[i],math[i]))

student_score.sort(key=lambda x: (-x.k, -x.e, -x.m))

for student in student_score:
    print(student.n,student.k,student.e,student.m)