import re


def has_consecutive_characters(word):
    for i in range(len(word)):
        chunk = word[i : i + 3]
        for index, j in enumerate(chunk):
            if index + 2 >= len(chunk):
                continue
            elif (
                ord(chunk[index]) - ord(chunk[index + 1]) == -1
                and ord(chunk[index + 1]) - ord(chunk[index + 2]) == -1
            ):
                return True
    return False


def has_double_letter(password):
    pattern = re.compile(r"(([a-zA-Z]))\2")
    pairs = set(pattern.findall(password))
    return len(pairs) >= 2


def is_valid(password):
    return (
        has_consecutive_characters(password)
        and not any(letter in ["i", "o", "l"] for letter in password)
        and has_double_letter("".join(password))
    )


if __name__ == "__main__":
    inp = "hepxxyzz"
    password = list(inp)
    current_index = -1

    while "".join(password) == inp or not is_valid(password):
        if (
            ord(password[current_index]) == 122
            and (ord(password[current_index]) + 1 - 97) % 26 + 97 == 97
        ):
            new_char = chr((ord(password[current_index]) + 1 - 97) % 26 + 97)
            password[current_index] = new_char
            if current_index - 1 >= -len(password):
                current_index -= 1
                continue
            else:
                break

        new_char = chr((ord(password[current_index]) + 1 - 97) % 26 + 97)
        password[current_index] = new_char

        current_index = -1

    print("".join(password))
