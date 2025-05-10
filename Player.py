from Sprite import Sprite
from Missile import Missile
import math
class Player(Sprite):
  def __init__(self):
    Sprite.__init__(self)
    self.shape = 'classic'
    self.size = 30
    self.lives = 3
    self.score = 0
    self.missiles = [] #move fire missile to player
  def draw(self, pen):
    pen.fd(9)
    pen.pendown() 
    pen.pensize(2)
    pen.right(158.5)
    pen.fd(18)
    pen.penup()
    pen.bk(18)
    pen.pendown()
    pen.right(42.5)
    pen.fd(18)
    pen.pendown()
    pen.bk(3.5)
    pen.left(112)
    pen.fd(10)
    pen.penup()
  def rotate_left(self):
    self.heading += 15
  def rotate_right(self):
    self.heading -= 15
  def accelerate(self):
    ax = math.cos(math.radians(self.heading))
    ay = math.sin(math.radians(self.heading))
    self.dy += ay 
    self.dx += ax 
  def decelerate(self):
    self.dy *= 0.99
    self.dx *= 0.99
  def update(self):
    Sprite.update(self)
    self.decelerate()
    for i in range(len(self.missiles)-1, -1,-1):
      if not self.missiles[i].active:
        self.missiles.pop(i)
  def fire_missile(self):
    if self.active:
      missile = Missile()
      self.missiles.append(missile)
      missile.fire(self)
      print(len(self.missiles))