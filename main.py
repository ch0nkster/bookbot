with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

alphabet = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

for x in file_contents:
    if x.lower() in alphabet: 
        alphabet[x.lower()] += 1

converted = []

for key, value in alphabet.items():
    converted.append([key, value])

sorted = converted.sort()

print('--- Begin report of books/frankenstein.txt ---')
print(f'{len(words)} word found in the document\n')
for letter in converted:
    print(f'The {letter[0]} character was found {letter[1]} times')
