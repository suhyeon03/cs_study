class info_person:
    def __init__(self, name, height, weight):
        self.na = name
        self.he = height
        self.we = weight

n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
student = []

for i in range(5):
    student.append(info_person(name[i], height[i], weight[i]))

people_name_sorted = sorted(student, key=lambda x: x.na)

people_height_sorted = sorted(student, key=lambda x: x.he, reverse=True)

print("name")
for person in people_name_sorted:
    print(f"{person.na} {person.he} {person.we}")

print("\nheight")
for person in people_height_sorted:
    print(f"{person.na} {person.he} {person.we}")