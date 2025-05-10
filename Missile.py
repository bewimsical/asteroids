import math
from Sprite import Sprite

class Missile(Sprite):
  def __init__(self):
    Sprite.__init__(self)
    self.size = 5 
    self.active = True

   
  def draw(self, pen):
    pen.pensize(self.size) 
    pen.bk(1)
    pen.pendown()
    pen.fd(1)
    pen.penup()
  def fire(self, player):
    # if not self.active:
    #   self.active = True
    self.x, self.y = (player.x, player.y)
    self.heading = player.heading
    self.dx = math.cos(math.radians(self.heading)) *2
    self.dy = math.sin(math.radians(self.heading)) *2 
  def update(self):
    if self.active:
      self.x += self.dx
      self.y += self.dy
      
      if self.x > 400:
        self.active = False
      elif self.x < -400:
        self.active = False
      if self.y > 300:
        self.active = False
      elif self.y < -300:
        self.active = False