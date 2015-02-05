#!/usr/bin/env python

import webbrowser
import os
import re

# Base HTML template for entire page
base_template = open('templates/base_template.html', 'r')
# HTML template for a single movie entry
tile_template = open('templates/movie_tile_template.html', 'r')

# read and separate templates
main_page_head, main_page_content = base_template.read().split('<!-- head-body split line -->')
movie_tile_content = tile_template.read()

base_template.close()
tile_template.close()

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            genre=movie.genre,
            running_time=movie.running_time,
            my_comment=movie.my_comment,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)