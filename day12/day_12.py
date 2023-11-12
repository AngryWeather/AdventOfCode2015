import re


def sum_numbers(numbers):
    return sum(numbers)


def main():
    input = ""

    with open("input.txt") as f:
        input = f.read()

    r = re.compile(r"-?\d+")
    numbers = list(map(int, r.findall(input)))

    print(sum_numbers(numbers))


if __name__ == "__main__":
    main()
