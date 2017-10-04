import turtle

def draw_square():

	# Getting a screen.
	window = turtle.Screen()
	window.bgcolor("black")

	# Getting a turtle
	mike = turtle.Turtle()
	chazzy = turtle.Turtle()

	mike.shape("arrow")
	mike.color("white")
	mike.speed(2)

	chazzy. shape("turtle")
	chazzy.color("blue")
	chazzy.speed(2)

	# Getting the directions and moving it 
	mike.forward(120)
	mike.right(90)

	mike.forward(120)
	mike.right(90)

	mike.forward(120)
	mike.right(90)

	mike.forward(120)
	mike.right(90)

	chazzy.circle(120)

	window.exitonclick()

draw_square()



