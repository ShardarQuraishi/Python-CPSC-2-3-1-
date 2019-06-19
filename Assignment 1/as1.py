#Shardar Mohammed Quraishi
#ID: 30045559
#CPSC 231
#assignment 1
#importing and setting turtle screen
import turtle
display=turtle.Screen()
display.setworldcoordinates(-180, -180, 950, 950)
#inputs
xc, yc = eval(input())
r = eval(input())
x1, y1 = eval(input())
x2, y2 = eval(input())
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
b = (2 * ((x1 - xc) * (x2 - x1) + (y1 - yc) * (y2 - y1)))
c = ((x1 - xc) ** 2 + (y1 - yc) ** 2 - r ** 2)

#finding all the intersections
alfapos = (-b + (b ** 2 - 4 * (a * c)) ** 0.5) / (2 * a)
alfaneg = (-b - (b ** 2 - 4 * (a * c)) ** 0.5) / (2 * a)
dis = b ** 2 - 4 * a * c

x_p1 = (1 - alfapos) * x1 + alfapos * x2
x_p2 = (1 - alfaneg) * x1 + alfaneg * x2
y_p1 = (1 - alfapos) * y1 + alfapos * y2
y_p2 = (1 - alfaneg) * y1 + alfaneg * y2

#setting turtle for small circles in intersection points
def arrow_1():
    arrow = turtle.Turtle()

    arrow.penup()
    arrow.goto(x_p1, y_p1)
    arrow.right(90)
    arrow.forward(10)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(10)
    arrow.penup()
    arrow.goto(x_p2, y_p2)
    arrow.right(90)
    arrow.forward(10)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(10)
def arrow_2():
    arrow = turtle.Turtle()
    arrow.penup()
    arrow.goto(x_p1, y_p1)
    arrow.right(90)
    arrow.forward(10)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(10)


#setting turtle for drawing circle and line
def arrow_drawcircle():
    arrow = turtle.Turtle()
    arrow.penup()
    arrow.goto(xc, yc)
    arrow.right(90)
    arrow.forward(r)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(r)
    arrow.penup()
    arrow.goto(x1, y1)
    arrow.right(90)
    arrow.forward(10)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(10)
    arrow.penup()
    arrow.goto(x1, y1)
    arrow.pendown()
    arrow.goto(x2, y2)
    arrow.penup()
    arrow.right(90)
    arrow.forward(10)
    arrow.left(90)
    arrow.pendown()
    arrow.circle(10)


def main():

    arrow_drawcircle()

main()

#setting all the conditional statements
if dis > 0 and alfapos > 0 and alfaneg > 0:
    arrow_1()
elif dis > 0 and alfapos< 1 and alfaneg < 0:
	arrow_2()
elif dis > 0  and alfapos>1 and alfaneg<0:
    arrow_drawcircle()
elif dis == 0:
    arrow_2()

else:
	print ('None')
turtle.exitonclick()
