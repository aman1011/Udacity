import turtle

def draw_figure():

	# get window speicification
	window = turtle.Screen()
	window.bgcolor("red")
	

	# get the turtle specifications
	mike = turtle.Turtle()
	mike.color("yellow")
	mike.speed(2)
	mike.shape("arrow")

	# draw a square and shift it be 10 degrees
	# repeat the step for 36 times.
	for i in range(1, 37):
	
		# draw a square
		sides = 0;
		while (sides < 4):
			mike.forward(120)
			mike.right(90)
			sides+= 1

		mike.right(10)

	window.exitonclick()


draw_figure()
