from movie import Movie
from user import User

my_movie = Movie("The Matrix", "Comedy", True)
user = User("Jose")
user.movies.append(my_movie)

print(my_movie.name)
print(my_movie.genre)
print(my_movie.watched)

print(user)

print(user.watched_movies())