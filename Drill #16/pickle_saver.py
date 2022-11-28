class npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y


yuri = npc('yuri', 100, 100)
print(yuri.__dict__)
yuri.__dict__['age'] = 30
print(yuri.name, yuri.x, yuri.y, yuri.age)

new_data = { 'name':'jenny', 'x':5, 'y':100, 'age':30}
yuri.__dict__.update(new_data)
print(yuri.name, yuri.x, yuri.y, yuri.age)

tom = npc('tom', 100, 200)
print(tom.__dict__)
npc_list = [yuri, tom]

import pickle

with open('npc.pickle', 'wb') as f:
    pickle.dump(npc_list, f)
