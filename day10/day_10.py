from collections import Counter


def solution():
    input = list(str(3113322113))
    iterations = 50
    result = ""
    current = 0
    j = 0
    res = result

    while j < iterations:
        for i, k in enumerate(input):
            if i + 1 < len(input) and input[current] != input[i + 1]:
                counter = Counter(input[current:i+1])
                current = i + 1

            if i + 1 == len(input) and input[-1] == input[current]:
                counter = Counter(input[current:i+1])

            elif i + 1 == len(input) and input[-1] != input[current]:
                counter = Counter[input[-1]]

            for item in counter.items():
                result += str(item[1]) + item[0]

            counter.clear()

        j += 1
        current = 0
        input = list(result)
        res = result
        result = ""

    print("length: ", len(res))


solution()
