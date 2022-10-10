# f string: f strings for formatting
# r string: used to prevent the escape sequences in the string and use in raw string matching
# 

# Strings
shirt = "blue"

print(shirt)

store = "Nick's pizza shop"

store2 = 'Nick\'s pizza shop, the "best" there is'

print(store)
print(store2)

day = 30
month = 'OCT'
temp = 65

print("Today is OCT 21 and it's 65 degrees outside")

print(f"Today is {month} {day} and it's {temp} degrees outside")

day_name = "friday"

print(f"Today is {day_name}")


name = 'dheemanth'
print(name[::-1])

print(name[len(name)::-1])

letters = 'abcdefghijklmnopq'
print(letters[5])
print(letters[-4])
print(letters[7])

"""strings are immutable, you can’t insert a character directly into
one or change the character at a specific index."""
name = 'Henny'
# name[0] = 'P'
#Instead yiu b=need to use some combination of string functions
print(name)
name = name.replace('H', 'P')
print(name)

print(len(name))
empty = ""
print(len(empty))

#split
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
print(tasks.split())
print(name.split())

#combine using join
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_str = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_str)

#replace
setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a ', 'a famous ', 1)) # it replaces only one instance

#strip
world = "  earth  "
print(world.strip())
print(world.strip(' '))
print(world.rstrip())
print(world.lstrip())
print(world.strip('!'))
blurt = "What the...!!?"
print(blurt.strip('.?!'))

import string
print(string.whitespace)
print(string.punctuation)
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))

#Serach and select
poem = '''All that doth flow we cannot liquid name
... Or else would fire and water be the same;
... But that is liquid which is moist and wet
... Fire that property can never get.
... Then 'tis not cold that doth the fire put out
... But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('no'))

#They work the same if the substring is found. If it isn’t, find() returns -1 , and index() raises an exception.
word = 'the'
print(poem.find(word))
print(poem.index(word))
print(poem.rfind(word))
print(poem.rindex(word))

word = 'duck'
print(poem.find(word))
print(poem.rfind(word))
# print(poem.index(word)) #this will through an exception 
# print(poem.rindex(word)) # this will throw an exception 

word = 'the'
print(poem.count(word))

print(poem.isalnum())

#Case
setup = 'a duck goes into a bar...'

print(setup.strip(string.punctuation))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.title().swapcase())

#Alignment
print(setup.center(30))
print(setup.ljust(30)) #left justify
print(setup.rjust(30)) #right justify

#String Foratting
#old style : %
# conversion types:
# %s string
# %x hex integer
# %d decimal  integer
# %o octal integer
# %f decimal float
# %e exponent float
# %g decimal or exponential float
# %% a literal %
print('%s'  %setup)
actor = 'richard'
cat = 'chester'
weight = 28
print("Our cat %s weighs %s pounds" % (cat, weight))

# New style : {} and format()
thing = 'woodchunk'
place = 'lake'
print('{}'.format(thing))
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))
print('The {thing} is in the {place}'.format(thing='duck', place='bathtub'))

d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))

#Newest style : f-strings
thing = 'wereduck'
place = 'werepond'
print(f'the {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')

# f-strings gain a new shortcut that’s helpful when
# you want to print variable names as well as their values. This is handy
# when debugging. The trick is to have a single = after the name in the {} -
# enclosed part of the f-string:
print(f'{thing = }, {place = }')
print(f'{thing[-4:] =}, {place.title() =}')

# things to do
song = """When an eel grabs your arm, And it causes great harm, That's - a moray!"""

song = song.replace('m','M')
print(song)