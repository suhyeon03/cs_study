n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class student:
    def __init__(self, name='', height=0, weight=0):
        self.n = name
        self.h = height
        self.w = weight

students = []
for i in range(n):
    students.append(student(name[i], height[i], weight[i]))

students.sort(key=lambda x: x.h)

for student in students:
    print(student.n, student.h, student.w)