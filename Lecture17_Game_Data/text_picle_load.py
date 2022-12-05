import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def show(self):
        print(f'Name:{self.name} @ {self.x}{self.y}')



with open ('npc.pickle', 'rb') as f:
    npcs = pickle.load(f)

for npc in npcs:
    npc.show()
