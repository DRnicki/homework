from turtle import  *
# area
# houses
# roofs
# doors
# windows
# moon
# stars

# AREA

speed(9)
color('blue')

penup()
goto(-400, 400)
pendown()

begin_fill()

for _ in range(4):
    forward(800)
    right(90)

end_fill()

# HOUSE'S-roof
fillcolor("yellow")
pencolor("black")

penup()
goto(-340, -130)
pendown()

begin_fill()

for i in range(4):
    forward(200)
    right(90)

end_fill()

fillcolor("white")
begin_fill()

left(45)
forward(140)
right(90)
forward(140)

end_fill()

# create window's
# 1 window
penup()
goto(-310, -150)
pendown()

right(45)

begin_fill()

for d in range(4):
    forward(40)
    left(90)

# 2 window

penup()
goto(-210, -150)
pendown()

for d in range(4):
    forward(40)
    left(90)

end_fill()

# door for our house

penup()
goto(-220,-240)
pendown()

fillcolor('black')
begin_fill()

for door in range(2):
    forward(70)
    right(90)
    forward(40)
    right(90)


end_fill()



# SECOND HOUSE


penup()
goto(-100, -130)
pendown()

fillcolor("brown")
begin_fill()

for SC in range(4):
    forward(200)
    left(90)

end_fill()

# roof

penup()
goto(-100, -130)
pendown()

fillcolor("red")
begin_fill()

right(225)
forward(140)
right(90)
forward(140)

end_fill()

# windows for 2thd house

penup()
goto(80, -150)
pendown()

right(45)

fillcolor("yellow")
begin_fill()

for wind in range(4):
    forward(40)
    right(90)


penup()
goto(-40, -150)
pendown()


for wind in range(4):
    forward(40)
    right(90)



end_fill()


# door for 2thd house

fillcolor('black')
begin_fill()


penup()
goto(20,-240)
pendown()

for door in range(2):
    forward(70)
    right(90)
    forward(40)
    right(90)


end_fill()


# ### 3thd house 
fillcolor("gray")
begin_fill()

penup()
goto(150,-130)
pendown()

left(90)

for i in range(4):
    forward(200)
    right(90)

end_fill()

# roof
fillcolor("purple")
begin_fill()

left(45)
forward(140)
right(90)
forward(140)

end_fill()

left(45)


# windows
fillcolor("orange")
begin_fill()


penup()
goto(180, -150)
pendown()

for wind in range(4):
    forward(40)
    right(90)

end_fill() 

begin_fill()

penup()
goto(280, -150)
pendown()

for wind in range(4):
    forward(40)
    right(90)

end_fill()



# door for 3thd house

fillcolor("black")
begin_fill()

penup()
goto(270,-240)
pendown()

right(90)

for door in range(2):
    forward(70)
    right(90)
    forward(40)
    right(90)

end_fill()

# # moon

fillcolor("gray")
begin_fill()


penup()
goto(270,240)
pendown()


circle(60)

end_fill()


# # star

penup()
goto(-170,240)
pendown()



color('white')    

begin_fill()

for _ in range(5):
    forward(100)   
    right(144)     

end_fill()

exitonclick()