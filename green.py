from constants import lanes, screen, background
from random import randint, choice
from GameObject import GameObject

class Green(GameObject):
 def __init__(self):
   super(Green, self).__init__(0, 0, './images/green.png')
   self.dx = 0
   self.dy = (randint(0, 200) / 100) + 1
   self.reset()

 def move(self):
   self.x += self.dx
   self.y += self.dy
   if self.y > 500:
    self.reset()

 def reset(self):
   self.x = choice(lanes)
   self.y = -64