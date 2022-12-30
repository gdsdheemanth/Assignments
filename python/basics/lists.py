#lists have order to them

from numpy import insert, number


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

#Lists
"""Lists are good for keeping track of things by their order, especially when
the order and contents might change. Unlike strings, lists are mutable.

You can change a list in place, add new elements, and delete or replace
existing elements. The same value can occur more than once in a list."""

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]

#in lists the values donot need to be unique
#create or combert with list 
another_empty_list = list()
#python list convers other iterbles datatypes like string, tuples, sets ets to list
print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

#create from a string with split()
splitme = 'a/b//c/d///e'
print(splitme.split('/'))

# Get an item by [offset]
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[-1])
print(marxes[0:2])

print(marxes)
marxes.reverse()
# The reverse() function changes the list but doesn’t return its value.
print(marxes)
marxes.append('zeppo')
print(marxes)
# when wanted to add item before any offset in the list use insert()
marxes.insert(2, 'gummo')
print(marxes)

print(['ssss'] * 3)

# Combine lists by using extend() or +
others = ['Gummo', 'karl']
marxes.extend(others)
print(marxes)

# change an item by offset
marxes[2] = 'wanda'
print(marxes)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

#delete an item with del
del marxes[-1]
print(marxes)