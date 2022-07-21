#lists have order to them

lis1 = [1,2,3,5,2, True, "name"]

fav_movies = ["mov1","mov2"]
print(fav_movies)
print(fav_movies[0])

print(len(fav_movies))

fav_movies.append("mov3")
print(fav_movies)

fav_movies.insert(1,"mov4")
print(fav_movies)

del(fav_movies[2])
print(fav_movies)

del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])

print(fav_movies)
