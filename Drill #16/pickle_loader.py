class npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y


import pickle

with open('npc.pickle', 'rb') as f:
    read_npc = pickle.load(f)

for i in range(2):
    print(read_npc[i].name, read_npc[i].x, read_npc[i].y)