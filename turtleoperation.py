import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range(100):
    t.color("green")
    t.forward(i*4)
    t.left(150)
    t.width(2)
    
turtle.done()
    

 