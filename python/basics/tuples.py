#Tuples are immutable
#When you asign elements to tuple, they can't be changed.

#create with commas and ()
empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

one_marx = ('Groucho',)
print(one_marx)
print(type(one_marx))

one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
print(type(marx_tuple))

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
print(type(marx_tuple))

#tuples let you assign multiple variables at once
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a,b,c = marx_tuple
#this is called tuple unpacking
print(a,b,c)

#create with tuple()
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

#combine tuples using +
print(('test1',) + ('test2', 'test3'))

#duplicate items with *
print(('yada',) * 3)

#compare tuples
a = (7,2)
b = (7,2,9)
print(a == b)
print(a <= b)
print(a < b)
print(a > b)
