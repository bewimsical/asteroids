from Sprite import Sprite
import random
import math

class Asteroid(Sprite):
  def __init__(self, x, y, sides = 11, size = 30):
    Sprite.__init__(self)
    self.x = x
    self.y = y
    self.shape = 'square'
    self.size = size
    self.tilt = 0
    self.spin = random.uniform(0.001,0.01)*random.choice([1,-1])
    self.is_split = False
    self.point_distance = []
    self.point_pos = []
    self.randomize_shape(sides)
    self.tier = 2 #TODO add this
    
  def randomize_shape(self,sides):
    for _ in range(sides):
      self.point_distance.append(random.uniform(0.5*self.size, self.size))
    px = self.x+self.point_distance[0]*math.cos(self.tilt)
    py = self.y+self.point_distance[0]*math.sin(self.tilt)
    angle = self.tilt
    self.point_pos.append((px,py))
    for i in range(sides-1):
      angle += 2* math.pi / sides
      px = self.x+self.point_distance[i+1]*math.cos(angle)
      py = self.y+self.point_distance[i+1]*math.sin(angle)
      self.point_pos.append((px,py))
    
  def draw(self, pen):
    pen.pensize(2)
    pen.penup()
    pen.goto(self.point_pos[0])
    pen.pendown()
    for i in range(1,len(self.point_pos)):
      pen.goto(self.point_pos[i])
    pen.goto(self.point_pos[0])
    pen.penup()
  
  def update(self):
    
    px = self.x+self.point_distance[0]*math.cos(self.tilt)
    py = self.y+self.point_distance[0]*math.sin(self.tilt)
    angle = self.tilt
    self.point_pos[0] =(px,py)
    for i in range(len(self.point_pos)-1):
      angle += 2* math.pi / len(self.point_pos)
      px = self.x+self.point_distance[i+1]*math.cos(angle)
      py = self.y+self.point_distance[i+1]*math.sin(angle)
      self.point_pos[i+1] = (px,py)
    super().update()
    
    self.tilt += self.spin

  def split(self):
    split = []
    sides = 10 if self.tier == 2 else 8
    size = 20 if self.tier == 2 else 10
    for _ in range(3):
      asteroid = Asteroid(self.x, self.y, sides, size)
      dx = random.randint(-5,5) / 20.0
      dy = random.randint(-5,5) / 20.0
      asteroid.dx = dx
      asteroid.dy = dy
      asteroid.tier = self.tier - 1
      split.append(asteroid)
    return split