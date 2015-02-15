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
                     "images/interstellar.jpg",
                     "http://youtu.be/0vxOhd4qlnA",
                     5,
                     "SF",
                     2*60+49)

frozen = Movie("Frozen",
               "The code never bothered me anyway",
               "images/frozen.jpg",
               "http://youtu.be/TbQm5doF_Uc",
               5,
               "Animation",
               108)

about_time = Movie("About Time",
                   "Rachel McAdams is so lovely!",
                   "images/about_time.jpg",
                   "http://youtu.be/T7A810duHvw",
                   5,
                   "Romance",
                   123)

sixty_sec = Movie("Gone in Sixty Seconds",
                  "1967 Shelby Mustang GT 500",
                  "images/60sec.jpg",
                  "http://youtu.be/cxCE9gDm1vo",
                  5,
                  "Action",
                  118)

groundhog_day = Movie("Groundhog Day",
                      "One of my favorite movies from my childhood",
                      "images/groundhog_day.jpg",
                      "http://www.youtube.com/watch?v=SZNuUzyVrmw",
                      5,
                      "Romantic Comedy",
                      101)

a_lot_like_love = Movie("A Lot Like Love",
                        "A lot like love story",
                        "images/alot_like_love.jpg",
                        "http://www.youtube.com/watch?v=1qLUMSbrlDE",
                        5,
                        "Romantic Comedy",
                        106)

constantine = Movie("Constantine",
                    "This is Constantine, John Constantine... a**hole",
                    "images/constantine.jpg",
                    "http://youtu.be/ivee8cm55Ao",
                    5,
                    "Fantasy",
                    120)

truman = Movie("The Truman Show",
               "In case I don't see ya, good afternoon, good evening, and good night!",
               "images/truman.jpg",
               "http://youtu.be/c3gI9ms8Fdc",
               5,
               "Drama",
               102)

hobbit_2 = Movie("The Hobbit: The Desolation of Smaug",
                 "The second of the Hobbit trilogy",
                 "images/hobbit2.jpg",
                 "http://youtu.be/OPVWy1tFXuc",
                 5,
                 "Fantasy",
                 2*60+41)

hobbit_1 = Movie("The Hobbit: An Unexpected Journey",
                 "I like this better than the LOR",
                 "images/hobbit1.jpg",
                 "http://youtu.be/SDnYMbYB-nU",
                 5,
                 "Fantasy",
                 2*60+49)

hobbit_3 = Movie("The Hobbit: The Battle of the Five Armies",
                 "More actions, less story",
                 "images/hobbit3.jpg",
                 "http://youtu.be/iVAgTiBrrDA",
                 5,
                 "Fantasy",
                 2*60+41)

inception = Movie("Inception",
                  "A dream in a dream in a dream",
                  "images/inception.jpg",
                  "http://youtu.be/8hP9D6kZseM",
                  5,
                  "SF",
                  2*60+27)

love_actually = Movie("Love Actually",
                      "Lots of famous actors",
                      "images/love_actually.jpg",
                      "http://youtu.be/KdzH6a-XEGM",
                      5,
                      "Romantic Comedy",
                      2*60+15)

wolf_of_wall_street = Movie("The Wolf of Wall Street",
                            "He really knows how to pick a movie",
                            "images/wolf.jpg",
                            "http://youtu.be/iszwuX1AK6A",
                            4.5,
                            "Drama",
                            179)

best_offer = Movie("The Best Offer",
                   "Old man's first love",
                   "images/best_offer.jpg",
                   "http://youtu.be/zJGleGyahC8",
                   4.5,
                   "Thriller",
                   131)

walter_mitty = Movie("The Secret Life of Walter Mitty",
                     "Great movie, but you can do better this Ben",
                     "images/walter.jpg",
                     "http://youtu.be/HddkucqSzSM",
                     4.5,
                     "Drama",
                     114)

penguins_of_madagascar = Movie("Penguins of Madagascar",
                               "Cute and cuddly penguins!",
                               "images/penguins.jpg",
                               "http://youtu.be/KHGHEpUeUwo",
                               4,
                               "Animation",
                               92)

x_men_dofp = Movie("X-MEN: Days of Future Past",
                   "Wolverine goes back in time",
                   "images/xmen_dofp.jpg",
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