# title director year 

# MENU_PROMPT ="  enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit: "
# loop

from time import sleep
import os

movies = []

def add_movie(movie_list):
    #movie = {"title":None, "director":None, "year":None}
    movie = {}
    title = input("Title: ")
    director = input("Director: ")
    year = input("Year: ")
    movie["title"]=title
    movie["director"]=director
    movie["year"]=year
    movie_list.append(movie)
    return movie

def show_movie(initial_text, movie):
   print(f"{initial_text} {movie['title']}, Director {movie['director']}, Year {movie['year']} ")   

def show_movies(movie_list):
   for movie in movie_list:
       #print(movie)
       show_movie("Movie info: ", movie)
       print("\n")

def find_movie(movies):
    movie_name = input("Enter movie title:")
    for movie in movies:
        if movie["title"] == movie_name:
            break;
    else:
        movie = None
    return movie

option_selected =  ""
while option_selected != "q":
    os.system('clear')
    option_selected = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title or 'q' to quit:")
    os.system('clear')
    if option_selected == 'a':
        added_movie = add_movie(movies)
        show_movie("New movie added  Title: ", added_movie)
        sleep(2)
    elif option_selected == 'l':
        #print(movies)
        show_movies(movies)
        sleep(3)
    elif option_selected == 'f':
        #print(movies)
        found_movie = find_movie(movies)
        if found_movie != None:
            show_movie("Movie Found!", found_movie)
        else:
            print("movie no found")
        sleep(3)    