import re


def evaluate_escaped_word(word):
    return count_escaped_characters(word) - count_characters_of_code(word)


def evaluate_word(word):
    return count_characters_of_code(word) - count_characters_in_string(word)


def count_words(words):
    sum = 0
    for word in words:
        sum += evaluate_escaped_word(word)

    return sum


def count_characters_of_code(word):
    return len(word)


def count_escaped_characters(word):
    count = 0
    quotes_count = 2
    r = re.compile(r'(\\|")')

    count = len(re.findall(r, word)) + len(word) + quotes_count
    # quotes_count accounts for enclosing quotes that remain unescaped

    return count


def count_characters_in_string(word):
    count = 0
    r = re.compile(r'(\\("|\\)|\\x[0-9a-fA-F]{2})')

    count += len(re.findall(r, word))
    new_word = re.sub(r, "", word).strip('\"')
    count += len(new_word)

    return count


if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            input.append(line.strip())

    print(count_words(input))
