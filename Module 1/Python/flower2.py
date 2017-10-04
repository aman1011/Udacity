import turtle

def make_project1():

	# Get the window details
	window = turtle.Screen()
	window.bgcolor("white")

	# Make a turtle
	mike = turtle.Turtle()
	mike.color("blue")
	mike.shape("turtle")
	mike.speed(30)

	# Repeat making a rhombus for 36 times with a
	# rotation of 10
	for i in range(1, 31):
		
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

		# making extra line.
		#mike.left(70)
		#mike.forward(60)
		#mike.backward(60)
		#mike.right(180)
		#mike.right(70)

		# tilting the rhombus with 10 degress
		mike.right(12)

	# getting the stem
	mike.right(90)
	mike.forward(300)

	window.exitonclick()

make_project1()



