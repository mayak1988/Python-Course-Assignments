# Create a script called count_words_in_lists.py that given a list of words (for now embedded in the program itself) will count how many times each word appears.
celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]
# Expected output:


# Moon        2
# Gas         1
# Asteroid    3
# Dwarf       1
word_dict = {}
for word in celestial_objects:
    if word in word_dict:
        word_dict[word]+=1
    else:
        word_dict[word]=1
for word, count in word_dict.items():
    print(f"{word:<12} {count}")
