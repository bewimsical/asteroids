import math

class Sprite():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.heading = 90
    self.dx = 0 
    self.dy = 0
    self.shape = 'square'
    self.color = 'white'
    self.size = 1.0
    self.active = True
    
  def update(self):
    if self.active:
      self.x += self.dx
      self.y += self.dy
      
      if self.x > 400:
        self.x = -400
      elif self.x < -400:
        self.x = 400
      if self.y > 300:
        self.y = -300
      elif self.y < -300:
        self.y = 300
    
  def render(self, pen):
    if self.active:
      pen.goto(self.x, self.y)
      pen.seth(self.heading)
      pen.shape(self.shape)
      pen.color(self.color)
      self.draw(pen)
    
  def draw(self, pen):
    pen.showturtle()
    pen.stamp()
    pen.hideturtle()
  
  def is_collision(self, other):
    x = self.x - other.x
    y = self.y - other.y
    distance = math.sqrt((x**2) + (y**2)) #pythag theorum to calc distance btwn 2 points
    if distance < ((self.size/2) + (other.size/2)) and self.active and other.active:
      return True
    else:
      return False