"""Count words in file."""


# put your code here.

def word_count(file):
    the_file = open(file)

    word_count = {}

    for line in the_file:
        words = line.strip().split(" ")
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

    the_file.close()

    for word, word_count in word_count.items():
        print(f"{word} {word_count}")
    
#word_count("test.txt")

word_count("twain.txt")