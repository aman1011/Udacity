import movie
import fresh_tomatoes

sorcerer_stone = movie.Movie("Harry Potter and the Sorcerer's Stone",
    "It's all in the J.K. Rowling's Harry Potter and the Sorcerer's Stone",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=VyHV0BRtdxo",
);

chamber_of_secret = movie.Movie("Harry Potter and the Chamber of secrets",
    "It's all in the J.K. Rowling's Harry Potter and the Chamber of Secrets",
    "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
    "https://www.youtube.com/watch?v=1bq0qff4iF8"
);

prisoner_of_azkaban = movie.Movie("Harry Potter and the Prisoner of Azkaban",
    "It's all in the J.K. Rowling's Harry Potter and the Prisoner of Azkaban",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
    "https://www.youtube.com/watch?v=lAxgztbYDbs"
);

goblet_of_fire = movie.Movie("Harry Potter and the Goblet of Fire",
    "It's all in the J.K. Rowling's Harry Potter and the Goblet of Fire",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
    "https://www.youtube.com/watch?v=3EGojp4Hh6I"
);

order_of_phoenix = movie.Movie("Harry Potter and the Order of Phoenix",
    "It's all in the J.K. Rowling's Harry Potter and the Order of Phoenix",
    "https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg",
    "https://www.youtube.com/watch?v=y6ZW7KXaXYk"
);

half_blood_prince = movie.Movie("Harry Potter and the Half-Blood Prince",
    "It's all in the J.K. Rowling's Harry Potter and the Half-Blood Prince",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg/220px-Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",
    "https://www.youtube.com/watch?v=sg81Lts5kYY"
);

deathly_hallow_first = movie.Movie("Harry Potter and the Deathly Hallows - Part 1",
    "It's all in the J.K. Rowling's Harry Potter and the Deathly Hallows - Part 1",
    "https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
    "https://www.youtube.com/watch?v=MxqsmsA8y5k"
);

deathly_hallow_second = movie.Movie("Harry Potter and the Deathly Hallows - Part 2",
    "It's all in the J.K. Rowling's Harry Potter and the Deathly Hallows - Part 2",
    "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
    "https://www.youtube.com/watch?v=mObK5XD8udk"
);

# using fresh_tomatoes method to display as website.
movies = [sorcerer_stone, chamber_of_secret, prisoner_of_azkaban, goblet_of_fire, order_of_phoenix, half_blood_prince, deathly_hallow_first, deathly_hallow_second]

# call the already built function,
#fresh_tomatoes.open_movies_page(movies)

# printing the newly defined class variable.
print(movie.Movie.VALID_RATINGS)
