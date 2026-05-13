# Incomplete app!

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# You may want to create a function for this code
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


# Create other functions for:

def print_movie(m):
    print(m['title'])
    print(m['director'])
    print(m['year'])

    
#   - listing movies
def list_movies():
    for m in movies:
        print_movie(m)

#   - finding movies
def find_movies(criterion, value):
    for m in movies:
        if criterion == 'title'
            if m['title'] == value
                print_movie(m)
        elif criterion == 'director'
            if m['director'] == value
                print_movie(m)
        elif criterion == 'year'
            if m['year'] = value
                print_movie(m)


# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie()
    elif selection == "l":
        list_movies();
    elif selection == "f":
        criterion = input('enter criterion: ')
        value = input('enter value to select movie: ')
        find_movies(criterion, value)
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
