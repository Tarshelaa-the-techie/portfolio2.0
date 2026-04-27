import turtle

t = turtle.Turtle()
t.speed(3)

# Title
t.penup()
t.goto(-80,180)
t.write("Sales Chart",font=("Arial",16,"bold"))

values=[100,150,80]
labels=["A","B","C"]

x=-120

for i in range(len(values)):
    t.goto(x,-100)
    t.pendown()

    # Draw bar
    for j in range(2):
        t.forward(40)
        t.left(90)
        t.forward(values[i])
        t.left(90)

    # Label below bar
    t.penup()
    t.goto(x+10,-120)
    t.write(labels[i])

    x+=70

turtle.done()