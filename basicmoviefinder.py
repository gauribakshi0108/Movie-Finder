MENU_PROMPT="\nEnter 'a' to add a movie, 'l' to see your movies,'f' to find a movie by title, or 'q' to quit:"
movies=[]
def add_movie():
    title=input("Enter a movie title:")
    director=input("Enter a movie director:")
    year=input("Enter movie release year:")

    movies.append({
        'title':title,
        'director':director,
        'year':year
    })

def show_movies():
    for  movie in movies:
        print(f"Name: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie ['director']}")
    print(f"Release year: {movie ['year']}")

def find_movie():
    search_title=input("Enter movie title you're looking for:")

    for movie in movies:
        if movie["title"]==search_title:
            print_movie(movie)
        else:
            print_movie("Movie not found. Try again!")
            
def menu():
    selection=input(MENU_PROMPT)
    while selection!="q":
        if selection=="a":
            add_movie()
        elif selection=="l":
            show_movies()
        elif selection=="f":
            find_movie()
        else:
            print("Unkonwn command. Please try again")
        
        selection=input(MENU_PROMPT)
        
menu()
