class adress:
    def __init__(self, name, street_address, region):
        self.na = name
        self.st = street_address
        self.re = region

n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)


liveing_g = []

for i in range(n):
    liveing_g.append(adress(name[i],street_address[i], region[i]))

liveing_g.sort(key=lambda x: x.na, reverse=True)
first_person = liveing_g[0]
print(f'name {first_person.na}\naddr {first_person.st}\ncity {first_person.re}', end=' ')

