class Parent():

    """ This is a parent class with last name and eye-color. """
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name is " + self.last_name)
        print("Eye color is " + self.eye_color)


class Child(Parent):

    """ This is a child class inheriting last name and eye color
        from the parent and having an additional instance variable
        called number of toys. """
    def __init__(self, last_name, eye_color, no_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.no_of_toys = no_of_toys


# instantiating the class.
billy_joe = Parent("joe", "blue")
billy_joe.show_info()

#print(billy_joe.last_name)

# instantiating the class child.
#silly_joe = Child("joe", "blue", 5)
#print(silly_joe.last_name)
#print(silly_joe.no_of_toys)
