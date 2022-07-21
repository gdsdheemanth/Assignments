cats = {"jane":6, "tom":4, "sara":2}
print(cats)

print(cats['tom'])

cats["new"] = 3

del(cats["sara"])

print(cats)

cats["tom"] = 10

text = """a b e t g f f a e"""

word_count = {}
for letter in text.split():
    if letter in word_count:
        word_count[letter] += 1
    else:
        word_count[letter] = 1

print(word_count)
