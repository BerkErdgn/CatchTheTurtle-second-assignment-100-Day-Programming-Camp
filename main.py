import turtle
import time
import random


def add_score(x, y):
    global score
    score +=1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", font=style, align="Center")


def counter_down(counter_time):
    timer_turtle.clear()
    style = ("Courier", 30, "italic")

    if counter_time > 0:
        timer_turtle.write(f"Time: {counter_time}", align="Center", font=style)
        game_screen.ontimer(lambda : counter_down(counter_time - 1), 1000)
        for i in range(2):
            x = random.randrange(-300, 300, 1)
            y = random.randrange(-300, 300, 1)
            moving_turtle.setpos(x, y)
            time.sleep(0.5)

    else:
        moving_turtle.hideturtle()
        timer_turtle.write("Game Over", align="Center", font=style)


game_screen = turtle.Screen()
game_screen.title("Catch The Turtle")
game_screen.bgcolor("#FFB300")

#Score Yazısı için
score = 0
score_turtle = turtle.Turtle()
#turtle'ı gizlemek için
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.setpos(0,350)
score_turtle.color("Red")
style = ("Courier", 30, "italic")
score_turtle.write(f"Score: {score}", font=style, align="Center")

#Timer ayarlama
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.setpos(0, 300)
timer_turtle.color("Red")

#Turtleların rastgele yerlere gelmesi

moving_turtle = turtle.Turtle()
moving_turtle.shape("turtle")
moving_turtle.color("green")
moving_turtle.shapesize(2, 2)
moving_turtle.penup()
moving_turtle.speed(10)
moving_turtle.onclick(add_score)

counter_down(30)

turtle.mainloop()

