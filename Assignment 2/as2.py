#Shardar Mohammed Quraishi
#UCID: 30045559
#22 Oct 2017
#Assignment 2

#importing turtle and random modules

import turtle
import random


count = 0;
scorekeeper = turtle.Turtle();

#defining function for Alex which will move taking specific inputs from the user inorder to move
def Alex_movement(Alex):
	u=30
	k=45
	direction = input("please enter direction: ")
	if(direction == "w"):
		Alex.forward(u)
	elif(direction == "a"):
		Alex.left(k)
	elif(direction == "d"):
		Alex.right(k)
	elif(direction == "s"):
		Alex.bk(u)
	else:
		print('Invalid response, TRY AGAIN!')
		return False
#counting the number of times Alex was moved.    
	global count
	
	count = count+1;
	scorekeeper.clear()
	scorekeeper.penup()
	scorekeeper.hideturtle()
	scorekeeper.setposition(50, -300)
	scorestring = "Number of times Alex was moved: %d" %count
	scorekeeper.write(scorestring,False, align="left", font=("Arial", 14, "normal"))

	
#defining function for the movement of Alice. Where 2/3rd of Alice's movement is forward and the rest is either right or left.
def Alice_movement(Alice):
	g=20
	b=90
	movement = random.randint(1,3)
	angle = random.randint(1,2)
	if(movement != 3):
		Alice.forward(g)
	else:
		if(angle == "1"):
			Alice.right(b)
		else:
			Alice.left(b)

#defining a function for calculating the distance between the Alex and Alice			
def check_distance(turtle1, turtle2):
	distance = turtle1.distance(turtle2)
	return distance

#defining a function where the game is run, Alex and Alice functions are called. There is a while loop in which the contents are run until the conditions are fulfilled.	
def play(turtle1, turtle2):
	while (check_distance(turtle1, turtle2) > 30):
		Alex_movement(turtle1)
		Alice_movement(turtle2)
	#setting up commands for the distance between the two turtles to be displayed on the turtle screen.
		global distance
		distance = turtle1.distance(turtle2)
		scorekeeper.setposition(-300, 300)
		distance = turtle1.distance(turtle2)
		distancestring = "Distance between Alex & Alice: %d" %distance
		scorekeeper.write(distancestring,False, align="left", font=("Arial", 14, "normal"))
	print(":.:Game over:.: Alex caught Alice:.:")
#this is the main function which calls upon all the functions defined and plays a major rule for the smooth running of the program. This also contains turtle and the screen properties.
def main():		
	tScreen = turtle.Screen()
	WIDTH = 500
	HEIGHT = 500
	tScreen.screensize(WIDTH,HEIGHT)
	Alex = turtle.Turtle()
	Alex.color("Blue")
	Alex.shape("turtle")

	Alice = turtle.Turtle()
	Alice.color("Red")
	Alice.shape("turtle")
	x1 = random.randint(-250, 250)
	y1 = random.randint(-250, 250)
	
	Alice.pu()
	Alice.setposition(x1, y1)
	Alice.pd()
	play(Alex, Alice)
	#print(check_distance(Alex, Alice))
	print("Number of times Alex was moved ", count)
		
	tScreen.mainloop()
	
main()
