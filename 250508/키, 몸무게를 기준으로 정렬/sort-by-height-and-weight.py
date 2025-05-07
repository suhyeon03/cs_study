class info_person:
    def __init__(self, name, height, weight):
        self.na = name
        self.he = height
        self.we = weight


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
student = []

for i in range(n):
    student.append(info_person(name[i], height[i], weight[i]))

people_sorted = sorted(student, key=lambda x: (x.he, -x.we))

for person in people_sorted:
    print(f"{person.na} {person.he} {person.we}")