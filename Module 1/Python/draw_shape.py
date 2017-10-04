import turtle

def draw_shape(shape):

	# windows specification.
	window = turtle.Screen()
	window.bgcolor("black")
	

	# turtle speicification
	mike = turtle.Turtle()
	mike.color("red")
	mike.speed(2)
	mike.shape("turtle")

	if (shape == 'square'):
		sides = 0
		while (sides<4):
			mike.forward(120)
			mike.right(90)
			sides += 1

	elif (shape == 'circle'):
		mike.circle(60)

	else:
		sides = 0
		while(sides<3):
			mike.right(120)
			mike.forward(120)
			sides += 1
		window.exitonclick()

draw_shape('square')
draw_shape('circle')
draw_shape('triangle')