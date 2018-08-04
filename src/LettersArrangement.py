import math


def get_letters_count(word):
    letters_count = {}
    for letter in word:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return letters_count


def count_permutations(word):
    return math.factorial(len(word))


def count_different_arrangements(word):
    letters_count = get_letters_count(word)
    identical_permutations_div = 1
    for letter in letters_count:
        identical_permutations_div *= math.factorial(letters_count[letter])
    return count_permutations(word) / identical_permutations_div


def remove_one_occurence(letter, letters_count):
    dic = dict(letters_count)
    if letter in dic:
        if dic[letter] > 1:
            dic[letter] -= 1
        else:
            del dic[letter]
    return dic


def print_letters_arrangements(word, letters_count):
    if len(letters_count) == 0:
        print word
    else:
        for letter in letters_count:
            print_letters_arrangements(
                word + letter,
                remove_one_occurence(letter, letters_count)
            )


def print_all_arrangements(word):
    if len(word) == 0:
        return
    if len(word) == 1:
        print word
        return
    letters_count = get_letters_count(word)
    print_letters_arrangements('', letters_count)


def print_letters_permutations(first, rest):
    if len(rest) == 0:
        print first
    else:
        [print_letters_permutations(first + letter, rest.replace(letter, '', 1)) for letter in rest]


def print_all_permutations(word):
    if len(word) == 0:
        return
    if len(word) == 1:
        print word
        return
    print_letters_permutations('', word)


def print_arrangements_count(word):
    print "There are " + str(count_different_arrangements(word)) + " different arrangements of letters in word " + word


print_arrangements_count("BOOKKEEPER")
print_arrangements_count("MISSISSIPPI")
print_arrangements_count("AAA")

print_arrangements_count("AABBCC")
print_all_arrangements("AABBCC")



