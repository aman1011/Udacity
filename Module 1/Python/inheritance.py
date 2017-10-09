class Parent():

    """ This is a parent class with last name and eye-color. """
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

# instantiating the class.
billy_joe = Parent("joe", "blue")
print(billy_joe.last_name)
