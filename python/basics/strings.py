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
print('Found and signing book deals:', crypto_string)
