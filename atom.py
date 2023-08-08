import turtle

# create a turtle to draw the atom
atom = turtle.Turtle()

# create a turtle to draw the electrons
electron1 = turtle.Turtle()
electron2 = turtle.Turtle()
electron3 = turtle.Turtle()

# set the turtle speed to the maximum
atom.speed(0)
electron1.speed(0)
electron2.speed(0)
electron3.speed(0)

# draw the nucleus of the atom
atom.circle(20)

# move the electrons to their starting positions
electron1.up()
electron1.goto(-40, 0)
electron1.down()

electron2.up()
electron2.goto(40, 0)
electron2.down()

electron3.up()
electron3.goto(0, 60)
electron3.down()

# set the angle for the electrons to rotate around the nucleus
angle = 0

# create an infinite loop to animate the electrons
while True:
    # rotate the electrons around the nucleus
    electron1.setheading(angle)
    electron2.setheading(angle + 120)
    electron3.setheading(angle + 240)

    # move the electrons in a circle around the nucleus
    electron1.circle(40, 3)
    electron2.circle(40, 3)
    electron3.circle(40, 3)

    # update the angle for the next iteration
    angle += 3
