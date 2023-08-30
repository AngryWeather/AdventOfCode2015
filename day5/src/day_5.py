def get_nice_strings_counter(words):
    counter = 0
    for word in words:
        if is_string_nice(word):
            counter += 1
    return counter


def is_string_nice(word):
    if not contains_wrong_strings(word):
        if has_enough_vowels(word) and has_double_letter(word):
            return True
    return False


def contains_wrong_strings(word):
    wrong_strings = ("ab", "cd", "pq", "xy")
    return any([x in word for x in wrong_strings])


def has_enough_vowels(word):
    vowels = ("a", "e", "i", "o", "u")
    return (len([x for x in word if x in vowels])) >= 3


def has_double_letter(word):
    index = 0
    while index < len(word):
        if word[index] == word[index + 1]:
            return True
        index += 1
        if index == len(word) - 1:
            return False
    return False


if __name__ == "__main__":
    words = []

    with open("input.txt", "r") as f:
        for line in f.readlines():
            words.append(line.strip())
    print(get_nice_strings_counter(words))
