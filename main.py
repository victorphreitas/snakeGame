from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("The Snake Game!")
screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# To make sure it hasnt colided to itself
is_on = True


def first_three():
    for position in positions:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        segments.append(segment)


first_three()

xcor = random.randint(-210, 211)
ycor = random.randint(-210, 211)

food = Turtle("circle")
food.color("blue")
food.turtlesize(0.5)

snake_speed = 15

# putting text into the screen
counter = 0
last_record = 1

text = Turtle("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 225)


def score():
    global counter, text
    text.clear()
    text.write(f"Score = {counter}", font=("Arial", 14, "normal"), align="center")
    counter += 1


def gameover():
    global last_record
    over = Turtle("square")
    over.color("red")
    over.penup()
    over.hideturtle()
    over.goto(0, 0)
    if counter > last_record:
        over.color("white")
        last_record = counter - 1
        over.write(f"Congratulations!\nYou beat the record!\nThe current record is {last_record}",
                   font=("Arial", 14, "normal"), align="center")
    else:
        over.write(f"Game Over! You're stupid as fuck!\nThe current record is: {last_record}",
                   font=("Arial", 14, "normal"), align="center")


def up():
    if int(segments[0].heading()) == 0:
        segments[0].right(-90)
    elif int(segments[0].heading()) == 180:
        segments[0].left(-90)
    segments[0].forward(15)


def down():
    if int(segments[0].heading()) == 0:
        segments[0].right(90)
    elif int(segments[0].heading()) == 180:
        segments[0].left(90)
    segments[0].forward(15)


def left():
    if int(segments[0].heading()) == 270:
        segments[0].right(90)
    if int(segments[0].heading()) == 90:
        segments[0].right(-90)
    segments[0].forward(15)


def right():
    if int(segments[0].heading()) == 270:
        segments[0].right(-90)
    if int(segments[0].heading()) == 90:
        segments[0].right(90)
    segments[0].forward(15)


# still not working because of the int function
def touch_body():
    global is_on
    for i in range(len(segments) - 2, 1, -1):
        if segments[0].distance(segments[i]) < 10:
            screen.title("Snake is dead!")
            is_on = False
            gameover()


def extend():
    # now i need to relocate the food
    new_xcor = random.randint(-210, 211)
    new_ycor = random.randint(-210, 211)
    food.penup()
    food.goto(new_xcor, new_ycor)
    # extra segment to the snake
    segment_extra = Turtle("square")
    segment_extra.color("white")
    segment_extra.hideturtle()
    segment_extra.penup()
    segments.append(segment_extra)
    segment_extra.showturtle()


def snake_movement(speed):
    global is_on, counter
    val = 0.1
    while segments[0].xcor() < 240 and segments[0].xcor() > -240 and segments[0].ycor() > -240 and segments[
        0].ycor() < 240 and is_on:
        screen.onkey(up, "Up")
        screen.onkey(down, "Down")
        screen.onkey(left, "Left")
        screen.onkey(right, "Right")

        if abs(int(segments[0].xcor()) - int(food.xcor())) <= 10 and abs(
                int(segments[0].ycor()) - int(food.ycor())) <= 10:
            score()
            extend()
        # fix int function so it can detect touch on body
        touch_body()
        segments[0].forward(speed)
        time.sleep(val)
        screen.update()
        for i in range(len(segments) - 1, 0, -1):
            new_x = segments[i - 1].xcor()
            new_y = segments[i - 1].ycor()
            segments[i].goto(new_x, new_y)
        screen.listen()
    else:
        screen.title("Snake is dead!")
        is_on = False
        gameover()


if is_on:
    snake_movement(speed=snake_speed)


# keeping the screen locked
screen.exitonclick()
