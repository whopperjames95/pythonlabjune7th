current_movies = {
    "die hard": "11:00am",
    "die hard 2": "1:00pm",
    "die hard 3": "3:00pm",
}

print("were showing the following moves:")
for key in current_movies:
    print(key)

movie = input("what movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("requested showtime isnt playing.")
else:
    print(movie, "is playing at", showtime)