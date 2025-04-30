user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class user:
    def __init__(self, user_id='', user_leval=0 ):
        self.i = user_id
        self.l = user_leval

user1 = user()
user1.user_id = 'codetree'
user1.user_leval = 10

user2 = user()
user2.user_id = user2_id
user2.user_leval = user2_level

print('user {} lv {}'.format(user1.user_id, user1.user_leval))
print('user {} lv {}'.format(user2.user_id, user2.user_leval))

