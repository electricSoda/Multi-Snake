import turtle
bgp = turtle.Turtle()
bgp.speed(5)
bgp.pensize(5)
bgp.color('black', 'black')
bgp.begin_fill()
bb = 0
while bb < 4:
    bgp.right(90)
    bgp.forward(200)
    bb += 1
bgp.end_fill()