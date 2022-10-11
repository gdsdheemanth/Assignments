from itertools import count


count = 1
while count <= 5:
    print(count)
    count+=1

while True:
    stuff = input('string to capitalize [type q to quit]: ')
    if stuff == 'q':
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':  #quit
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)

numbers = [1,3,5,6,7]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    else:
        print('no even number found at position', position)
    position += 1

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

#better way is usinf for loop
#string iteration will produce one character at a time
for letter in word:
    print(letter)

word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

word = 'thudx'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

# For loop number sequences with range()
for x in range(0,3):
    print(x)

print(list(range(0,3)))

for x in range(2,-1,-1):
    print(x)

print(list(range(0,11,2)))

print(list(range(3,-1,-1)))

guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it')
        break
    else:
        print('oops')
    number +=1


