unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class solve_boom:
    def __init__(self, unlock_code, wire_color, seconds):
        self.u = unlock_code
        self.w = wire_color
        self.e = seconds

solve_boom1 = solve_boom(unlock_code, wire_color, seconds)

print(f"code : {solve_boom1.u}")
print(f"color : {solve_boom1.w}")
print(f"second : {solve_boom1.e}")