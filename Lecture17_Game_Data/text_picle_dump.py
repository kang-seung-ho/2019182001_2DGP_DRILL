import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def show(self):
        print(f'Name:{self.name} @ {self.x}{self.y}')


yuri = NPC('Yuri', 100, 200)



yuri.name = 'tom'

yuri.__dict__.update({'name':'jeni', 'x':100, 'y':100})

print(yuri.__dict__) #모든 객체는 __dict__ 라는 내부 변수가 존재

# tom = NPC('Tom', 200, 100)
# npcs = [yuri, tom]
# yuri.show()
# 
# with open ('npc.pickle', 'wb') as f:
#     pickle.dump(npcs, f)
