import turtle

print("Hint: To create a well-structured and visually balanced tree, consider the following:")
print("- Left and right branch angles should ideally be between 15 and 45 degrees.")
print("- Starting branch length should generally be at least 50 for a visible tree.")
print("- Recursion depth should be at least 3 to create enough branching.")
print("- Branch length reduction factor (%) should usually range from 50 to 80.")
print("- Experiment wi20th the values to achieve different tree shapes and sizes!\n")


left_angle = int(input('Left branch angle: '))
right_angle = int(input('Right branch angle: '))
branch_length = int(input('Stating branch length: '))
recursion_depth = int(input('Recursion depth: '))
reduction_factor = float(input('Branch length reduction factor (%): ')) / 100

# setup the screen and the turtle
screen = turtle.Screen()
screen.screensize(600, 600)
t = turtle.Turtle()
t.pensize(3)


def draw(length, depth):
    # if max branching depth reached, return with drawing
    if depth == 0:
        return
    # draw the central stem
    t.forward(length)
    t.color('green')
    # save branching position
    branch_point = t.pos()
    branch_heading = t.heading()

    # draw the left branch recursively
    t.left(left_angle)
    draw(length * reduction_factor, depth - 1)
    # return to saved branching position
    t.penup()
    t.setpos(branch_point)
    t.setheading(branch_heading)
    t.pendown()
    # draw the right branch recursively
    t.right(right_angle)
    draw(length * reduction_factor, depth - 1)


# go to bottom of the screen and set heading up
t.penup()
t.goto(0, -300)
t.setheading(90)
t.pendown()

# start drawing with starting branch length and recursion depth
t.color('brown')
draw(branch_length, recursion_depth)

t.hideturtle()
turtle.exitonclick()
