import turtle
import random


def game_start(x, y):
    game_screen.clear()
    game_screen.title("Catch The Turtle")
    game_screen.bgcolor("#FFB300")

    score_turtle = turtle.Turtle()
    moving_turtle = turtle.Turtle()
    timer_turtle = turtle.Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.setpos(0, 300)
    timer_turtle.color("Red")

    def make_scoreboard():
        score_turtle.hideturtle()
        score_turtle.penup()
        score_turtle.setpos(0, 350)
        score_turtle.color("Red")
        score_turtle.write(f"Score: {score}", font=style, align="Center")

    def counter_down(counter_time):
        timer_turtle.clear()
        style = ("Courier", 30, "italic")

        if counter_time > 0:
            timer_turtle.write(f"Time: {counter_time}", align="Center", font=style)
            game_screen.ontimer(lambda: counter_down(counter_time - 1), 1000)

        else:
            moving_turtle.hideturtle()
            timer_turtle.write("Game Over", align="Center", font=style)

    def add_score(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", font=style, align="Center")

    def moving_turtle_fonk():
        turtle.tracer(0)
        moving_turtle.shape("turtle")
        moving_turtle.color("green")
        moving_turtle.shapesize(2, 2)
        moving_turtle.penup()
        moving_turtle.speed(10)
        moving_turtle.onclick(add_score)
        x = random.randrange(-300, 300, 1)
        y = random.randrange(-300, 300, 1)
        moving_turtle.setpos(x, y)
        game_screen.ontimer(moving_turtle_fonk, 500)
        turtle.tracer(1)

    make_scoreboard()
    moving_turtle_fonk()
    counter_down(30)


#gamescreen
game_screen = turtle.Screen()
game_screen.title("Catch The Turtle")
game_screen.bgcolor("#FFB300")

score = 0

game_name_turtle= turtle.Turtle()
style2 = ("Courier", 35, "italic")
game_name_turtle.penup()
game_name_turtle.setpos(0,35)
game_name_turtle.hideturtle()
game_name_turtle.write("Catch The Turtle", font=style2, align="center")

start_turtle = turtle.Turtle()
style = ("Courier", 35, "italic")
start_turtle.penup()
start_turtle.setpos(0,20)
start_turtle.write("Click the turtle to start", font=("Courier", 10, "italic"), align="center")
start_turtle.hideturtle()


start_turtle_image = turtle.Turtle()
start_turtle_image.penup()
start_turtle_image.shape("turtle")
start_turtle_image.color("green")
start_turtle_image.onclick(game_start)


turtle.mainloop()

