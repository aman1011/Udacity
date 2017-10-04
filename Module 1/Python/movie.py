class Movie():

    # Every class has a init function
    # otherwise known as constructor
    # which gets called upon while creating
    # an instance or object.
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = movie_poster_image
        self.trailer = movie_trailer
