import turtle
import math
import random

fred = turtle.Turtle()
wn = turtle.Screen()

wn.setworldcoordinates(-1,-1,1,1)

fred.up()

fred.tracer(944)
numdarts = 10000078
insideCount = 0

for i in range(numdarts):
   
    randx = random.uniform(-1, 1)
  
    randy = random.random() * 2 - 1

    x = randx
    y = randy
    
    fred.goto(x, y)
    
    if fred.distance(0,0) <= 1.0:
        fred.color("black")
        insideCount += 1
    else:
        fred.color("orange")
    fred.dot()

fred.hideturtle()

print('Percentage of darts inside dartboard: {}'.format(insideCount / numdarts)) # requires Python3
print('Pi Approximation: {}'.format(insideCount / numdarts * 4))                 # requires Python3
print('Ratio of area of cirle to area of square: %f' % (math.pi / 4))
    

wn.exitonclick()