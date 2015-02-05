#!/usr/bin/env python

from media import Movie
import fresh_tomatoes

"""
## Movie class parameters
  - title
  - my comment
  - poster image
  - trailer
  - my rating
  - genre
  - running time
"""

interstellar = Movie("Interstellar",
                     "The best movie I've watched in 2014",
                     "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg",
                     "http://youtu.be/0vxOhd4qlnA",
                     5,
                     "SF",
                     2*60+49)

frozen = Movie("Frozen",
               "The code never bothered me anyway",
               "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SX214_AL_.jpg",
               "http://youtu.be/TbQm5doF_Uc",
               5,
               "Animation",
               108)

about_time = Movie("About Time",
                   "Rachel McAdams is so lovely!",
                   "http://ia.media-imdb.com/images/M/MV5BMTA1ODUzMDA3NzFeQTJeQWpwZ15BbWU3MDgxMTYxNTk@._V1_SX214_AL_.jpg",
                   "http://youtu.be/T7A810duHvw",
                   5,
                   "Romance",
                   123)

sixty_sec = Movie("Gone in Sixty Seconds",
                  "1967 Shelby Mustang GT 500",
                  "http://ia.media-imdb.com/images/M/MV5BMTIwMzExNDEwN15BMl5BanBnXkFtZTYwODMxMzg2._V1_SY317_CR1,0,214,317_AL_.jpg",
                  "http://youtu.be/cxCE9gDm1vo",
                  5,
                  "Action",
                  118)

groundhog_day = Movie("Groundhog Day",
                      "One of my favorite movies from my childhood",
                      "http://images.moviepostershop.com/groundhog-day-movie-poster-1993-1020189656.jpg",
                      "http://www.youtube.com/watch?v=SZNuUzyVrmw",
                      5,
                      "Romantic Comedy",
                      101)

a_lot_like_love = Movie("A Lot Like Love",
                        "A lot like love story",
                        "http://movieposters.2038.net/p/A-Lot-Like-Love.jpg",
                        "http://www.youtube.com/watch?v=1qLUMSbrlDE",
                        5,
                        "Romantic Comedy",
                        106)

constantine = Movie("Constantine",
                    "This is Constantine, John Constantine... a**hole",
                    "http://ia.media-imdb.com/images/M/MV5BMTE5NDk5NTUyN15BMl5BanBnXkFtZTYwNzUyMDA3._V1_SX214_AL_.jpg",
                    "http://youtu.be/ivee8cm55Ao",
                    5,
                    "Fantasy",
                    120)

truman = Movie("The Truman Show",
               "In case I don't see ya, good afternoon, good evening, and good night!",
               "http://ia.media-imdb.com/images/M/MV5BMTM4NjY2MTEzM15BMl5BanBnXkFtZTcwMTk2Njk3OA@@._V1_SX214_AL_.jpg",
               "http://youtu.be/c3gI9ms8Fdc",
               5,
               "Drama",
               102)

hobbit_2 = Movie("The Hobbit: The Desolation of Smaug",
                 "The second of the Hobbit trilogy",
                 "http://ia.media-imdb.com/images/M/MV5BMzU0NDY0NDEzNV5BMl5BanBnXkFtZTgwOTIxNDU1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                 "http://youtu.be/OPVWy1tFXuc",
                 5,
                 "Fantasy",
                 2*60+41)

hobbit_1 = Movie("The Hobbit: An Unexpected Journey",
                 "I like this better than the LOR",
                 "http://ia.media-imdb.com/images/M/MV5BMTcwNTE4MTUxMl5BMl5BanBnXkFtZTcwMDIyODM4OA@@._V1_SX214_AL_.jpg",
                 "http://youtu.be/SDnYMbYB-nU",
                 5,
                 "Fantasy",
                 2*60+49)

hobbit_3 = Movie("The Hobbit: The Battle of the Five Armies",
                 "More actions, less story",
                 "http://ia.media-imdb.com/images/M/MV5BODAzMDgxMDc1MF5BMl5BanBnXkFtZTgwMTI0OTAzMjE@._V1_SX214_AL_.jpg",
                 "http://youtu.be/iVAgTiBrrDA",
                 5,
                 "Fantasy",
                 2*60+41)

inception = Movie("Inception",
                  "A dream in a dream in a dream",
                  "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg",
                  "http://youtu.be/8hP9D6kZseM",
                  5,
                  "SF",
                  2*60+27)

love_actually = Movie("Love Actually",
                      "Lots of famous actors",
                      "http://ia.media-imdb.com/images/M/MV5BMTY4NjQ5NDc0Nl5BMl5BanBnXkFtZTYwNjk5NDM3._V1_SX214_AL_.jpg",
                      "http://youtu.be/KdzH6a-XEGM",
                      5,
                      "Romantic Comedy",
                      2*60+15)

wolf_of_wall_street = Movie("The Wolf of Wall Street",
                            "He really knows how to pick a movie",
                            "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX214_AL_.jpg",
                            "http://youtu.be/iszwuX1AK6A",
                            4.5,
                            "Drama",
                            179)

best_offer = Movie("The Best Offer",
                   "Old man's first love",
                   "http://ia.media-imdb.com/images/M/MV5BMTQ4MzQ3NjA0N15BMl5BanBnXkFtZTgwODQyNjQ4MDE@._V1_SX214_AL_.jpg",
                   "http://youtu.be/zJGleGyahC8",
                   4.5,
                   "Thriller",
                   131)

walter_mitty = Movie("The Secret Life of Walter Mitty",
                     "Great movie, but you can do better this Ben",
                     "http://ia.media-imdb.com/images/M/MV5BODYwNDYxNDk1Nl5BMl5BanBnXkFtZTgwOTAwMTk2MDE@._V1_SX214_AL_.jpg",
                     "http://youtu.be/HddkucqSzSM",
                     4.5,
                     "Drama",
                     114)

penguins_of_madagascar = Movie("Penguins of Madagascar",
                               "Cute and cuddly penguins!",
                               "http://ia.media-imdb.com/images/M/MV5BMTEyMDg4MDU4MjdeQTJeQWpwZ15BbWU4MDQyOTc3MjIx._V1_SX214_AL_.jpg",
                               "http://youtu.be/KHGHEpUeUwo",
                               4,
                               "Animation",
                               92)

x_men_dofp = Movie("X-MEN: Days of Future Past",
                   "Wolverine goes back in time",
                   "http://ia.media-imdb.com/images/M/MV5BMjEwMDk2NzY4MF5BMl5BanBnXkFtZTgwNTY2OTcwMDE@._V1_SX214_AL_.jpg",
                   "http://youtu.be/pK2zYHWDZKo",
                   4.0,
                   "SF",
                   134)

# List of all movies
movies = [
    interstellar,
    frozen,
    about_time,
    sixty_sec,
    groundhog_day,
    a_lot_like_love,
    constantine,
    truman,
    hobbit_2,
    hobbit_1,
    hobbit_3,
    inception,
    love_actually,
    wolf_of_wall_street,
    best_offer,
    walter_mitty,
    penguins_of_madagascar,
    x_men_dofp,
]

# create a new HTML file with movie data
# this will open a new page in your browser
fresh_tomatoes.open_movies_page(movies)