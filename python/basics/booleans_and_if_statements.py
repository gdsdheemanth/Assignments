day = 30
month = 'OCT'
temp = 65

light_is_on = False

if light_is_on:
    print("light is ON")
print("Hello")

switch = False

if switch:
    print("switch is on")
else:
    print("we are in dark")

weight = 79.65

if weight < 80 :
    print("you are underweight :)")
else:
    print("over weight")

letter = 'o'

vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list)

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

vowel_dict = {'a': 'apple', 'e': 'elephant','i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict)

vowel_string = "aeiu"
print(letter in vowel_string)


#Assignment

import random

secret = 5
guess = random.randint(1,10)

if guess < secret :
    print(f"{guess} is too low")
elif guess > secret :
    print(f"{guess} is too high")
else:
    print("just right")