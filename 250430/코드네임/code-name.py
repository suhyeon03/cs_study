MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class Agent:
    def __init__(self, codename='', score=0):
        self.c = codename
        self.s = score

users = []
for i in range(MAX_N):
    users.append(Agent(codenames[i], scores[i]))

min_idx = 0
for i in range(1,5):
    if users[min_idx].s > users[i].s:
        min_idx = i

print(users[min_idx].c, users[min_idx].s)