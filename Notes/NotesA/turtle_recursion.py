import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

my_screen = turtle.Screen()
my_screen.bgcolor('white')


# draw a shape using goto

my_turtle.fillcolor('red')
my_turtle.begin_fill()  # starts a shape to fill in

my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.up()
my_turtle.goto(-200,-200)
my_turtle.end_fill()
my_turtle.down()
my_turtle.fillcolor('blue')
my_turtle.begin_fill()
my_turtle.goto(0,0)
my_turtle.goto(0, -200)
my_turtle.goto(-200, -200)
my_turtle.end_fill()
my_turtle.goto(0, 0)


my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(4)
my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
my_turtle.setheading(90)


for i in range(12):
    my_turtle.forward(50)
    my_turtle.left(30)
my_turtle.end_fill()

my_turtle.speed()



my_screen.clear()
my_turtle.home()

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)  # top right
        my_turtle.down()
        my_turtle.goto(width / 2, -height / 2)  # bottom right
        my_turtle.goto(-width / 2, -height / 2) # bottom left
        my_turtle.goto(-width / 2, height/ 2 ) # top left
        my_turtle.goto(width / 2, height / 2)  # top right
        recursive_rect(width / 333, height / 333, depth - 1)

recursive_rect(300, 300, 5)

my_screen.exitonclick()





