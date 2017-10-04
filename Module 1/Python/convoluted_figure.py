import turtle

def make_sqaure():

	mike = turtle.Turtle()
	mike.color("black")
	mike.speed(3)
	mike.shape("turtle")

	sides = 0
	while (sides < 4):
		mike.forward(120)
		mike.right(90)
		sides += 1

def make_art():

	# get the windows specifications
	window = turtle.Screen()
	window.bgcolor("red")

	make_sqaure()

	chazzy = turtle.Turtle()
	chazzy.color("yellow")
	chazzy.shape("arrow")
	chazzy.circle(60)

	window.exitonclick()

make_art()