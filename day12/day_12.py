import json


def sum_of_item(item, skip_red=False):
    if isinstance(item, list):
        return sum([sum_of_item(i, skip_red) for i in item])

    if isinstance(item, dict):
        if skip_red and "red" in item.values():
            return 0
        return sum([sum_of_item(i, skip_red) for i in item.values()])

    if isinstance(item, str):
        return 0

    if isinstance(item, int):
        return item


with open("input.txt") as f:
    abacus = json.load(f)
print(sum_of_item(abacus))
print(sum_of_item(abacus, skip_red=True))
