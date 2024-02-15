import turtle

turtle.shape('turtle')
turtle.pencolor('blue')

turtle.speed(10)
size = 5

for i in range(0, 60):
    turtle.circle(size)
    turtle.left(5)
    size = size + 10

turtle.mainloop()