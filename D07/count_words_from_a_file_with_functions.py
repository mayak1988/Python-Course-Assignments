def count_words(filename):
    word_count = {}

    with open(filename, 'r') as f:
        for line in f:
            
            line = line.strip().lower()
            
            words = line.split()
            
            for word in words:
                if word not in word_count:
                    word_count[word] = 0
                word_count[word] += 1

    return word_count

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python count_words_from_a_file.py your_text_file.txt")
        exit(1)

    filename = sys.argv[1]
    counts = count_words(filename)

    print("Word counts:")
    for word in sorted(counts.keys()):
        print(f"{word}: {counts[word]}")