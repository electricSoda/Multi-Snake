#Multi-Snake
#game.py

#import modules
import time
import turtle
import random
from tkinter import *
import sys
import winsound
import os
import mainScreen
import os.path
import struct

#working directory
os.chdir("C:\\teleport\\Code\\Multi-Snake")

#popup window
NORM_FONT = ("Helvetica", 10)
def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    w=400
    h=100
    ws = popup.winfo_screenwidth()
    hs = popup.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
    popup.iconbitmap(r'alert_vSg_icon.ico')
    label = Message(popup, text=msg, font=NORM_FONT, aspect = 700)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="OK", command = popup.destroy)
    B1.pack()
    popup.mainloop()

stop_bool = False

# gameloop
gameloop = True

#delay
delay = 0.1

# Score
score1 = 0
high_score1 = 0
score2 = 0
high_score2 = 0

#encase the code in snake()
def snake():
    global wn, stop_bool
    stop_bool = True

    pe = True

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

    #define pause bool
    pausebool = True

    def paused():
        global pause, pe, pausebool, gameloop
        v1 = struct.pack('>d', high_score1)
        v2 = struct.pack('>d', high_score2)
        gameloop = False
        pe = False
        pausebool = False
        # try:
        #     a1 = os.path.isfile('config1.msk')
        #     a2 = os.path.isfile('config2.msk')
        #     if a1 == False:
        #         with open('config1.msk', 'wb+') as h1:
        #             h1.write(v1)
        #             h1.close()
        #     else:
        #         with open('config1.msk', 'rb') as h1:
        #             reade1 = h1.read()
        #             str(reade1)
        #             aa1 = b'%b' % reade1
        #             u1 = struct.unpack('>d', aa1)
        #             u1 = int(u1[0])
        #             print(u1)
        #             if u1 < high_score1:
        #                 c1 = open("config1.msk", "wb+")
        #                 c1.write(v1)
        #                 c1.close()
        #             else:
        #                 d1 = open('config1.msk', 'wb+')
        #                 d1.write(aa1)
        #                 d1.close()
        #     if a2 == False:
        #         with open('config2.msk', 'wb+') as h2:
        #             h2.write(v2)
        #             h2.close()
        #     else:
        #         with open('config2.msk', 'rb') as h2:
        #             reade2 = h2.read()
        #             str(reade2)
        #             aa2 = b'%b' % reade2
        #             u2 = struct.unpack('>d', aa2)
        #             u2 = int(u2[0])
        #             print(u2)
        #             if u2 < high_score2:
        #                 c2 = open("config2.msk", "wb+")
        #                 c2.write(v1)
        #                 c2.close()
        #             else:
        #                 d2 = open('config2.msk', 'wb+')
        #                 d2.write(aa2)
        #                 d2.close()
        #
        # except Exception as e:
        #     popupmsg('An error occured whilst storing item/loading pause: %s' % e)
        #     print(e)

        #Pause the turtles
        a = int(len(segments1))
        b = int(len(segments2))
        del segments1[0:a]
        del segments2[0:b]
        head1.direction = "stop"
        head2.direction = "stop"

        #Create background for pause screen (turtle)
        # bgp = turtle.Turtle()
        # bgp.speed(5)
        # bgp.pensize(5)
        # bgp.shape('classic')
        # bgp.color('white', 'white')
        # bgp.goto(-450, 370)
        # bgp.begin_fill()
        # for i in range(2):
        #     bgp.forward(900)
        #     bgp.right(90)
        #     bgp.forward(740)
        #     bgp.right(90)
        # bgp.end_fill()
        # bgp.hideturtle()

        #hide the player and food turtles
        food1.hideturtle()
        food2.hideturtle()

        #Pen for writing pause menu
        penm = turtle.Turtle()
        penm.pensize(5)
        penm.color('black')
        penm.speed(5)
        penm.penup()
        penm.goto(0, 200)
        penm.pendown()
        penm.write('Game Paused', align="center", font=("Comic Sans MS", 60, "bold underline"))
        penm.penup()
        penm.goto(-250, 150)
        penm.color('black', 'light green')
        penm.pendown()
        penm.begin_fill()
        for i in range(2):
            penm.forward(500)
            penm.right(90)
            penm.forward(450)
            penm.right(90)
        penm.end_fill()
        penm.penup()
        penm.goto(0, 100)
        penm.pensize(5)
        def btn1(color1, color2):
            penm.goto(-200, 100)
            penm.pendown()
            penm.color(color1, color2)
            penm.begin_fill()
            for i in range(2):
                penm.forward(400)
                penm.right(90)
                penm.forward(100)
                penm.right(90)
            penm.end_fill()
            penm.penup()
            penm.goto(0, 30)
            penm.write('Continue Playing', align="center", font=("Comic Sans MS", 30, "bold"))

        def btn2(color1, color2):
            penm.goto(-200, -150)
            penm.color(color1, color2)
            penm.pendown()
            penm.begin_fill()
            for i in range(2):
                penm.forward(400)
                penm.right(90)
                penm.forward(100)
                penm.right(90)
            penm.end_fill()
            penm.penup()
            penm.goto(0, -225)
            penm.write('Main Menu', align="center", font=("Comic Sans MS", 30, "bold"))

        btn1('black', 'white')
        btn2('black', 'white')
        penm.hideturtle()

        #define cleared function
        def cleared():
            wn.clearscreen()
            wn.setup(0,0)
            wn.update()
            return


        def btnclick1(x, y):
            if x > -200 and x < 200 and y < 108 and y > 2:
                btn1('black', 'yellow')
                time.sleep(0.5)
                head1.showturtle()
                head2.showturtle()
                food1.showturtle()
                food2.showturtle()
                gameloop = True
                mainlp()
                penm.clear()
            else:
                pass

            if x > -200 and x < 200 and y < -147 and y > -250:
                btn2('black', 'yellow')
                time.sleep(0.5)
                gameloop = False
                cleared()
                mainScreen.startScrn('Multi-Snake', 'white')
                sys.exit()
            else:
                pass

        turtle.onscreenclick(btnclick1, 1)
        turtle.listen()


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
    def mainlp():
        while gameloop == True:
            global delay, score1, score2, high_score1, high_score2
            wn.update()

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
                if pausebool == True:
                    wn.onkeypress(paused, "Escape")
                else:
                    pass
            else:
                pass

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
                winsound.PlaySound("Pickup_Food.wav", winsound.SND_ASYNC)
                time.sleep(0.1)
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
                winsound.PlaySound("Pickup_Food.wav", winsound.SND_ASYNC)
                time.sleep(0.1)
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
                winsound.PlaySound("Pickup_Food.wav", winsound.SND_ASYNC)
                time.sleep(0.1)
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
                winsound.PlaySound("Pickup_Food.wav", winsound.SND_ASYNC)
                time.sleep(0.1)
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
    mainlp()

    #start the mainloop
    wn.mainloop()

#Exit/ stop function for the GUI
def stop():
    if stop_bool == False:
        sys.exit()
    else:
        wn.bye()
        sys.exit()