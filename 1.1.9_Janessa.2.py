import turtle as trtl
#create custom the turtle
trtl.addshape("star",((-10,10),(-2,0),(-10,-10),(0,-2),(10,-10),(2,0),(10,10),(0,2)))

# create the background
trtl.bgcolor("midnight blue")

#create grass 
trtl.hideturtle()
trtl.pensize(300)
trtl.pencolor("DarkOliveGreen4")
trtl.penup()
trtl.goto(-1000,-300)
trtl.pendown()
trtl.forward(10000)

#create stars and moon 

# create moon 
trtl.speed(100)
trtl.penup()
trtl.goto(300,100)
trtl.pendown()
trtl.pencolor("cornsilk2")
trtl.pensize(50)
trtl.begin_fill()
trtl.circle(100)
trtl.fillcolor("cornsilk2")
trtl.end_fill()

#create stars 
trtl.color("goldenrod1")
trtl.shape("star")
# i will do the rest later for the radom stars!

# create the tree

#create tree trunk
trtl.color("orange4")
trtl.hideturtle()
trtl.penup()
trtl.goto(300,-300)
trtl.pendown()
trtl.begin_fill()
trtl.circle(300,140)
trtl.right(140)
trtl.forward(200)
trtl.right(90)
trtl.forward(550)
trtl.right(90)
trtl.forward(390)
trtl.fillcolor("orange4")
trtl.end_fill()

#create leaves 
leave_colors = ["DarkRed","DarkGoldenrod2","DarkOrange4"]
trtl.begin_fill()
trtl.penup()
trtl.goto(450,300)
trtl.pencolor("DarkRed")
for leaves in range(3):
    trtl.fillcolor(leave_colors)
    trtl.pendown()
    trtl.circle(30)
trtl.end_fill()











wn = trtl.Screen()
wn.mainloop()