import turtle
#add a delay in the move loop to see the snake
import time
#import random module
import random
# This is the speed of the worm/snake
delay = 0.2

# Score
score = 0
high_score = 0
# setup the screen make a window on the screen

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('#2272A7')
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the screen updates

#test comment testing git
#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#22A73A")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
        if head.direction != "down":
            head.direction = 'up'
def go_down():
        if head.direction != "up":
            head.direction = 'down'

def go_left():
        if head.direction != "right":
            head.direction = 'left'

def go_right():
        if head.direction != "left":
            head.direction = 'right'


def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
            y = head.ycor()
            head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
             x = head.xcor()
             head.setx(x + 20)

#Keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop-this updates the screen -call the move function
while True:
    wn.update()

    # Check for collision with the border
    # if head goes off the screen to right, left, top or bottom then pause it, then send it to 0,0 and stop it
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments List
        segments.clear()

        # Reset the score after collision with border
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

#check for a collison with the food

    if head.distance(food) < 20:
        #move food to random spot on the screen if the distance from the head is less than 20 pixels
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Move the end segments first in reverse order
    for index in range(len(segments)-1, -1, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

# Move segment 0 first one after head to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)


    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments List
            segments.clear()
            # Reset the score after collision with border
            score = 0

            # Reset the delay
            delay = 0.1

            # Update score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

#keeps window open
#add comment for test commit