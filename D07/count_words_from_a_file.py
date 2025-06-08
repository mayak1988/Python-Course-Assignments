# Create a script called count_words_from_a_file.py that given a file with words and spaces and newlines only, count how many times each word appears.


# Lorem ipsum dolor qui ad labor ad labor sint dolor  tempor incididunt ut labor ad dolore lorem ad
# Ut labor ad dolor lorem qui ad ut labor   ut ad commodo commodo
# Lorem ad dolor in reprehenderit in lorem ut labor ad dolore eu in labor dolor
# sint occaecat ad labor proident sint in in qui labor ad dolor ad in ad labor

# Expected result for the above file:


# # examples/dictionary/words_and_spaces_counted.txt
               
# ad            13
# commodo        2
# dolor          6
# dolore         2
# eu             1
# in             6
# incididunt     1
# ipsum          1
# labor         10
# lorem          5
# occaecat       1
# proident       1
# qui            3
# reprehenderit  1
# sint           3
# tempor         1
# ut             5


import sys

if len(sys.argv) != 2:
    print("Usage: python count_words_from_a_file.py input.txt")
    exit(1)
else:
    input_filename = sys.argv[1]
    output_filename = "words_and_spaces_counted.txt"

    word_count = {}

    with open(output_filename, 'r') as f:
        for line in f:
            line = line.strip().lower()
            words = line.split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1





    with open(output_filename, 'w') as out_file:
        for word in sorted(word_count.keys()):
            out_file.write(f"{word}: {word_count[word]}\n")

    print(f"Word counts saved to '{output_filename}'")