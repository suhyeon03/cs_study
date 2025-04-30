secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class agent:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

agent1 = agent(secret_code, meeting_point, time)
print('secret code :',agent1.s)
print('meeting point :',agent1.m)
print('time :',agent1.t)