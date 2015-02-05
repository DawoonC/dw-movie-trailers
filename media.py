#!/usr/bin/env python

class Movie(object):
    """ This class provides a way to store movie related information """

    def __init__(self,
                 movie_title,
                 my_comment,
                 poster_image,
                 trailer_youtube,
                 my_rating,
                 genre,
                 running_time):
        self.title = movie_title
        self.my_comment = my_comment
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.my_rating = my_rating
        self.genre = genre
        self.running_time = running_time