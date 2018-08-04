import math


def get_letters_count(word):
    letters_count = {}
    for letter in word:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return letters_count


def count_different_arrangements(word):
    letters_count = get_letters_count(word)
    den = 1
    for letter in letters_count:
        den *= math.factorial(letters_count[letter])
    return math.factorial(len(word)) / den


def print_arrangements(word):
    print "There are " + str(count_different_arrangements(word)) + " different arrangements of letters in word " + word


print_arrangements("BOOKKEEPER")
print_arrangements("ABCD")
print_arrangements("AAA")
print_arrangements("MISSISSIPPI")

