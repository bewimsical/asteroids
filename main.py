import math
import turtle
import random
from Player import Player
from Asteroid import Asteroid

screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(800,600)

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.hideturtle()       
    
#main loop
screen.update()
screen.bgpic("title.png") 

#create a list of sprites
startGame = False
player = Player()
sprites = []

for _ in range(5):
  x = random.randint(-175, 175)
  y = random.randint(-175, 175)
  asteroid = Asteroid(x,y)
  dx = random.randint(-5,5) / 20.0
  dy = random.randint(-5,5) / 20.0
  asteroid.dx = dx
  asteroid.dy = dy
  sprites.append(asteroid)

def start(x,y):
  global startGame
  startGame = True
  
#key bindings
screen.listen()
screen.onkey(player.rotate_right, "Right")
screen.onkey(player.rotate_left, "Left")
screen.onkey(player.accelerate, "Up")
screen.onkey(player.decelerate, "Down")
screen.onkey(player.fire_missile, "space")
screen.onclick(start)
print(startGame)


grace_period = 0
max_grace_period = 100


#main loop
def game_loop():
    global grace_period
    global max_grace_period
    grace_period += 1

    pen.clear()

    for missile in player.missiles:
        missile.render(pen)
        missile.update()

    for sprite in sprites:
        sprite.render(pen)
        sprite.update()
    
  #check for colisions
    for sprite in sprites:
        if isinstance(sprite, Asteroid):
            if player.is_collision(sprite) and grace_period > max_grace_period:
                grace_period = 0
                player.lives -= 1
            #print("Lives: " + str(player.lives))
                if player.lives <= 0:
                #print("PLAYER DIES")
                    player.active = False  
                    player.x = 0
                    player.y = 0
            for missile in player.missiles:
                if missile.active and missile.is_collision(sprite):
            #print("ASTEROID DIES")
                    sprite.active = False
                    if sprite.tier > 0:
                        for sprite in sprite.split():
                            sprites.append(sprite)
                    missile.active = False
                    player.score += 10
         # print("Score: " + str(player.score))
        

  #draw score and lives
    x, y = -373, 240
    pen.goto(-380, 260)
    pen.write(str(player.score), False, font=("Courier New", 18, 'normal'))
    for i in range(player.lives):
        pen.goto(x,y)
        pen.seth(90)
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
        x+= 20
    if player.lives <= 0:
        pen.goto(0, 0)
        pen.write('Game Over', False, font=("Courier New", 25, 'normal'), align = 'center')

    screen.update()
    screen.ontimer(game_loop, 5)

def wait_for_start():
    pen.clear()
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()
    screen.update()
    if not startGame:
        screen.ontimer(wait_for_start, 0)
    else:
        screen.bgpic("nopic")  # remove background
        screen.bgcolor("black")
        sprites.append(player)
        game_loop()
      
wait_for_start()   
screen.mainloop()