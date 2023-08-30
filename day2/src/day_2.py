presents = []


def calculate_surface_area(present):
    return (2 * present["l"] * present["w"]) + (2 * present["w"] * present["h"]) + (2 * present["h"] * present["l"])


def find_area_of_smallest_side(present):
    return min((present["l"] * present["w"]), present["w"] * present["h"], present["h"] * present["l"])


def find_total(present):
    return calculate_surface_area(present) + find_area_of_smallest_side(present)


def find_total_for_all_presents(presents):
    total = 0

    for present in presents:
        total += find_total(present)

    return total


def find_ribbon_for_present(present):
    return min(find_face_perimeter(present["l"], present["w"]),
               find_face_perimeter(present["w"], present["h"]),
               find_face_perimeter(present["h"], present["l"]))


def find_face_perimeter(side_1, side_2):
    return 2 * side_1 + 2 * side_2


def find_ribbon_for_bow(present):
    return present["w"] * present["l"] * present["h"]


def find_total_feet_of_ribbon(present):
    return find_ribbon_for_present(present) + find_ribbon_for_bow(present)


def find_total_ribbon_for_all(presents):
    total = 0
    for present in presents:
        total += find_total_feet_of_ribbon(present)
    return total


with open("./input.txt", "r") as f:
    for line in f.readlines():
        present_temp = line.strip().split("x")
        present = {"l": int(present_temp[0]),
                   "w": int(present_temp[1]), "h": int(present_temp[2])}
        presents.append(present)

print(find_total_ribbon_for_all(presents))
