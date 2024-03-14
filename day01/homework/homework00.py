from turtle import *

width(4)
speed(8)

color('brown')
penup()
goto(-200, -300)
pendown() #for start position
begin_fill()

forward(400)
left(90)

forward(300)
left(90)

forward(400)
left(90)

forward(300)
left(90)  

end_fill()      # house squere

forward(160)
left(90)
color('gray')

begin_fill()

forward(150)
right(90)
forward(80)
right(90)
forward(150)  # this is a door

end_fill()

penup()
goto(200, 0)
pendown()


color('blue')   
begin_fill()
right(135)
forward(285)
left(90)
forward(285)
end_fill()

left(45)      # The roof

penup()
goto(-170, -50)
pendown()


color('yellow')   
begin_fill()
forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

end_fill()        # window 1

penup()
goto(170, -50)
pendown()

begin_fill()

forward(100)
right(90)

forward(100)
right(90)

forward(100)
right(90)

forward(100)
right(90)

end_fill()      #window 2


penup()
goto(150, 20)
pendown()

left(180)
color('black')
begin_fill()
forward(100)
left(90)

forward(30)
left(90)

forward(100)
left(90)

forward(30)
left(90)

end_fill()



exitonclick()