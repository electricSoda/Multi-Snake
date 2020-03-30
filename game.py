#Multi-Snake
#game.py

#import modules
import time
import pickle
import turtle
import random
import os

#working directory
os.chdir("C:\\teleport\\Code\\Multi-Snake")

#encase the code in snake()
def snake():
    delay = 0.1

    gameloop = True

    pe = True

    # Score
    score1 = 0
    high_score1 = 0
    score2 =0
    high_score2 = 0

    #set up the screen
    wn = turtle.Screen()
    wn.title("Multi-Snake")
    wn.bgcolor("dark green")
    wn.setup(width = 900, height = 740)
    wn.tracer(0) #Turns off screen updates

    #Snake head 1
    head1 = turtle.Turtle()
    head1.speed(0)
    head1.shape("square")
    head1.color("blue")
    head1.penup()
    head1.goto(-200, 0)
    head1.direction = "stop"

    #Snake head 2
    head2 = turtle.Turtle()
    head2.speed(0)
    head2.shape("square")
    head2.color("red")
    head2.penup()
    head2.goto(200, 0)
    head2.direction = "stop"

    #Snake Food 1
    food1 = turtle.Turtle()
    food1.speed(0)
    food1.shape("circle")
    food1.color("yellow")
    food1.penup()
    food1.goto(-150, 200)

    #Snake Food 2
    food2 = turtle.Turtle()
    food2.speed(0)
    food2.shape("circle")
    food2.color("yellow")
    food2.penup()
    food2.goto(150, 200)

    segments1 = []
    segments2 = []

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 320)
    pen.write("Player 1 : 0        Player 2 : 0", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, 290)
    pen.write("High Score : 0        High Score : 0", align="center", font=("Courier", 16, "normal"))

    #Functions
    #head1 functions
    def go_up1():
        if head1.direction != "down":
            head1.direction = "up"

    def go_down1():
        if head1.direction != "up":
            head1.direction = "down"

    def go_left1():
        if head1.direction != "right":
            head1.direction = "left"

    def go_right1():
        if head1.direction != "left":
            head1.direction = "right"

    #head2 functions
    def go_up2():
        if head2.direction != "down":
            head2.direction = "up"

    def go_down2():
        if head2.direction != "up":
            head2.direction = "down"

    def go_left2():
        if head2.direction != "right":
            head2.direction = "left"

    def go_right2():
        if head2.direction != "left":
            head2.direction = "right"

    def paused():
        try:
            pickle.dump(score1, open("score1.dat", "wb"))
            pickle.dump(high_score1, open("high1.dat", "wb"))
            pickle.dump(score2, open("score2.dat", "wb"))
            pickle.dump(high_score2, open("high2.dat", "wb"))
            pickle.dump(len(segments1), open("length1.dat", 'wb'))
            pickle.dump(len(segments2), open("length2.dat", "wb"))

        except:
            print("Something went wrong. Please try again later.")

        a = int(len(segments1))
        b = int(len(segments2))
        del segments1[0:a]
        del segments2[0:b]
        print(segments1)
        print(segments2)
        head1.direction = "stop"
        head2.direction = "stop"
        gameloop = False
        pe = False
        exit()




    #Keyboard bindings
    if pe == True:
        wn.listen()
        wn.onkeypress(go_up1, "w")
        wn.onkeypress(go_left1, "a")
        wn.onkeypress(go_down1, "s")
        wn.onkeypress(go_right1, "d")
        wn.onkeypress(go_up2, "Up")
        wn.onkeypress(go_left2, "Left")
        wn.onkeypress(go_down2, "Down")
        wn.onkeypress(go_right2, "Right")
        wn.onkeypress(paused, "Escape")
    else:
        pass

    #other functions

    def move1():
        if head1.direction == "up":
            y = head1.ycor()
            head1.sety(y + 20)

        if head1.direction == "down":
            y = head1.ycor()
            head1.sety(y - 20)

        if head1.direction == "left":
            x = head1.xcor()
            head1.setx(x - 20)

        if head1.direction == "right":
            x = head1.xcor()
            head1.setx(x + 20)

    def move2():
        if head2.direction == "up":
            y = head2.ycor()
            head2.sety(y + 20)

        if head2.direction == "down":
            y = head2.ycor()
            head2.sety(y - 20)

        if head2.direction == "left":
            x = head2.xcor()
            head2.setx(x - 20)

        if head2.direction == "right":
            x = head2.xcor()
            head2.setx(x + 20)


    #Main Game loop
    while gameloop == True:
        wn.update()

        # Check for a collision with teamate's segment (head1)
        for segment in segments2:
            if segment.distance(head1) < 20:
                time.sleep(1)
                head1.goto(-200, 0)
                head1.direction = "stop"
                head2.goto(200, 0)
                head2.direction = "stop"

                # Hide the segments
                for segment in segments1:
                    segment.goto(1000000000, 1000000000)

                for segment in segments2:
                    segment.goto(1000000000, 1000000000)

                # Clear the segments lists
                segments1.clear()
                segments2.clear()

                # Reset the delay
                delay = 0.1

                # Clear the score
                score1 = 0
                score2 = 0
                pen.goto(0, 320)
                pen.clear()
                pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
                pen.goto(0, 290)
                pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        # Check for a collision with teamate's segment (head2)
        for segment in segments1:
            if segment.distance(head2) < 20:
                time.sleep(1)
                head1.goto(-200, 0)
                head1.direction = "stop"
                head2.goto(200, 0)
                head2.direction = "stop"

                # Hide the segments
                for segment in segments1:
                    segment.goto(1000000000, 1000000000)

                for segment in segments2:
                    segment.goto(1000000000, 1000000000)

                # Clear the segments lists
                segments1.clear()
                segments2.clear()

                # Reset the delay
                delay = 0.1

                # Clear the score
                score1 = 0
                score2 = 0
                pen.goto(0, 320)
                pen.clear()
                pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
                pen.goto(0, 290)
                pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        # Check for a collision with the border (head1)
        if head1.xcor() > 440 or head1.xcor() < -440 or head1.ycor() > 340 or head1.ycor() < -340:
            time.sleep(1)
            head1.goto(-200, 0)
            head1.direction = "stop"
            head2.goto(200, 0)
            head2.direction = "stop"

            # Hide the segments
            for segment in segments1:
                segment.goto(1000000000, 1000000000)

            for segment in segments2:
                segment.goto(1000000000, 1000000000)

            # Clear the segments lists
            segments1.clear()
            segments2.clear()

            # Reset the delay
            delay = 0.1

            # Clear the score
            score1 = 0
            score2 = 0
            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        # Check for a collision with the border (head2)
        if head2.xcor() > 440 or head2.xcor() < -440 or head2.ycor() > 340 or head2.ycor() < -340:
            time.sleep(1)
            head1.goto(-200, 0)
            head1.direction = "stop"
            head2.goto(200, 0)
            head2.direction = "stop"

            # Hide the segments
            for segment in segments1:
                segment.goto(1000000000, 1000000000)

            for segment in segments2:
                segment.goto(1000000000, 1000000000)

            # Clear the segments lists
            segments1.clear()
            segments2.clear()

            # Reset the delay
            delay = 0.1

            # Clear the score
            score1 = 0
            score2 = 0
            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))


        #Check for a collision with the food1 (head1)
        if head1.distance(food1) < 20:
            #Move the food1 to a random spot
            x = random.randint(-440, 440)
            y = random.randint(-310, 310)
            food1.goto(x, y)

            #Add a segment
            new_segment1 = turtle.Turtle()
            new_segment1.speed(0)
            new_segment1.shape("square")
            new_segment1.color("cyan")
            new_segment1.penup()
            segments1.append(new_segment1)

            # Shorten the delay
            delay -=0.001

            # Increase the score
            score1 += 10

            if score1 > high_score1:
                high_score1 = score1

            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        #Check for a collision with the food1 (head2)
        if head2.distance(food1) < 20:
            #Move the food1 to a random spot
            x = random.randint(-440, 440)
            y = random.randint(-310, 310)
            food1.goto(x, y)

            #Add a segment
            new_segment1 = turtle.Turtle()
            new_segment1.speed(0)
            new_segment1.shape("square")
            new_segment1.color("orange")
            new_segment1.penup()
            segments2.append(new_segment1)

            # Shorten the delay
            delay -=0.001

            # Increase the score
            score2 += 10

            if score2 > high_score2:
                high_score2 = score2

            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        #Check for a collision with the food2 (head1)
        if head1.distance(food2) < 20:
            #Move the food2 to a random spot
            x = random.randint(-440, 440)
            y = random.randint(-310, 310)
            food2.goto(x, y)

            #Add a segment
            new_segment1 = turtle.Turtle()
            new_segment1.speed(0)
            new_segment1.shape("square")
            new_segment1.color("cyan")
            new_segment1.penup()
            segments1.append(new_segment1)

            # Shorten the delay
            delay -=0.001

            # Increase the score
            score1 += 10

            if score1 > high_score1:
                high_score1 = score1

            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))


        #Check for a collision with the food2 (head2)
        if head2.distance(food2) < 20:
            #Move the food2 to a random spot
            x = random.randint(-440, 440)
            y = random.randint(-310, 310)
            food2.goto(x, y)

            #Add a segment
            new_segment1 = turtle.Turtle()
            new_segment1.speed(0)
            new_segment1.shape("square")
            new_segment1.color("orange")
            new_segment1.penup()
            segments2.append(new_segment1)

            # Shorten the delay
            delay -=0.001

            # Increase the score
            score2 += 10

            if score2 > high_score2:
                high_score2 = score2

            pen.goto(0, 320)
            pen.clear()
            pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
            pen.goto(0, 290)
            pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))


        # Move in the segments (head1) first in reverse order
        for index in range(len(segments1)-1, 0, -1):
            x = segments1[index-1].xcor()
            y = segments1[index-1].ycor()
            segments1[index].goto(x, y)

        # Move in the segments (head2) first in reverse order
        for index in range(len(segments2)-1, 0, -1):
            x = segments2[index-1].xcor()
            y = segments2[index-1].ycor()
            segments2[index].goto(x, y)

        # Move segment 0 to where head1 is
        if len(segments1) > 0:
            x = head1.xcor()
            y = head1.ycor()
            segments1[0].goto(x, y)

        # Move segment 0 to where head2 is
        if len(segments2) > 0:
            x = head2.xcor()
            y = head2.ycor()
            segments2[0].goto(x, y)

        move1()
        move2()

        #Check for head1 collision with the body segments
        for segment in segments1:
            if segment.distance(head1) < 20:
                time.sleep(1)
                head1.goto(-200, 0)
                head1.direction = "stop"
                head2.goto(200, 0)
                head2.direction = "stop"

                # Hide the segments
                for segment in segments1:
                    segment.goto(1000000000, 1000000000)

                for segment in segments2:
                    segment.goto(1000000000, 1000000000)

                # Clear the segments lists
                segments1.clear()
                segments2.clear()

                # Reset the delay
                delay = 0.1

                # Clear the score
                score1 = 0
                score2 = 0
                pen.goto(0, 320)
                pen.clear()
                pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
                pen.goto(0, 290)
                pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))

        #Check for head2 collision with the body segments
        for segment in segments2:
            if segment.distance(head2) < 20:
                time.sleep(1)
                head1.goto(-200, 0)
                head1.direction = "stop"
                head2.goto(200, 0)
                head2.direction = "stop"

                # Hide the segments
                for segment in segments1:
                    segment.goto(1000000000, 1000000000)

                for segment in segments2:
                    segment.goto(1000000000, 1000000000)

                # Clear the segments lists
                segments1.clear()
                segments2.clear()

                # Reset the delay
                delay = 0.1

                # Clear the score
                score1 = 0
                score2 = 0
                pen.goto(0, 320)
                pen.clear()
                pen.write("Player 1 : {}        Player 2 : {}".format(score1, score2), align="center", font=("Courier", 18, "normal"))
                pen.goto(0, 290)
                pen.write("High Score : {}        High Score : {}".format(high_score1, high_score2), align="center", font=("Courier", 16, "normal"))


        time.sleep(delay)


    #start the mainloop
    wn.mainloop()
