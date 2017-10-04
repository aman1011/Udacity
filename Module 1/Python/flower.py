import turtle

def make_project1():

	# Get the window details
	window = turtle.Screen()
	window.bgcolor("white")

	# Make a turtle
	mike = turtle.Turtle()
	mike.color("blue")
	mike.shape("arrow")
	mike.speed(10)

	# Repeat making a rhombus for 36 times with a
	# rotation of 10
	for i in range(1, 37):
		
		# Making a rhombus
		mike.left(75)
		mike.forward(120)
		mike.right(150)
		mike.forward(120)
		mike.right(30)
		mike.forward(120)
		mike.right(150)
		mike.forward(120)

		# aligning
		mike.right(105)

		mike.left(5)
		mike.forward(60)

		# tilting the rhombus with 5 degress
		mike.right(5)
		mike.right(10)

	# getting the stem
	mike.left(90)
	mike.backward(180)

	window.exitonclick()

make_project1()

