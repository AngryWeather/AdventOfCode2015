import itertools


def calculate_total(perm):
    total = 0
    for n in range(len(perm)):
        # print(len(perm))
        # print(n, (n+1) % len(perm))
        total += relationship[(perm[n], perm[(n + 1) % len(perm)])]
        total += relationship[(perm[(n + 1) % len(perm)], perm[n])]
    return total


if __name__ == "__main__":
    input = []
    with open("input.txt") as f:
        for line in f.readlines():
            input.append(line)

    relationship = {}
    people = []

    people.append("me")

    for i in input:
        sentence = i.split()
        person = sentence[0]
        if person not in people:
            people.append(person)
            relationship[("me", person)] = 0
            relationship[(person, "me")] = 0
        target = sentence[10].strip(".")
        if sentence[2] == "gain":
            points = int(sentence[3])
        else:
            points = int(sentence[3]) * -1
        relationship[(person, target)] = points

        perm = list(itertools.permutations(people))

    max_total = 0
    for n in perm:
        total = calculate_total(n)
        max_total = max(max_total, total)
    print(max_total)
