'''

for döngüleri ile ilk başta aşağıdaki kodları yazdım. Fakat sonraki sürecde sorunlar yaşattılar.Budan dolayı buradaki kodları değitirdi.


def timer():
    for i in range(5, -1, -1):
        timer_turtle.clear()
        style = ("Courier", 30, "italic")
        timer_turtle.write(f"Time :{i}", font=style, align="Center")
        time.sleep(1)




def counterdown(countertime):
    turtle.clear()
    style = ("Courier", 30, "italic")

    if countertime > 0:
        timer_turtle.write(countertime, align="Center", font=style)
        game_screen.ontimer(lambda : counterdown(countertime - 1), 1000)
    else:
        timer_turtle.write("Game Over", align="Center", font=style)
        game_screen.ontimer(lambda x,y: counterdown(30))

game_screen.onclick(lambda x,y : counterdown(30))
'''
