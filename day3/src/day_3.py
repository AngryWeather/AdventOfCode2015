def find_houses(path):
    visited = [{"x": 0, "y": 0}]
    current_santa = {"x": 0, "y": 0}
    current_robo_santa = {"x": 0, "y": 0}

    for index, p in enumerate(path, start=1):
        turn = index % 2
        new_point = current_santa.copy() if (
            turn % index == 0) else current_robo_santa.copy()
        match p:
            case "^":
                new_point["y"] = current_santa["y"] + \
                    1 if turn % 2 == 0 else current_robo_santa["y"] + 1
            case ">":
                new_point["x"] = current_santa["x"] + \
                    1 if turn % 2 == 0 else current_robo_santa["x"] + 1
            case "v":
                new_point["y"] = current_santa["y"] - \
                    1 if turn % 2 == 0 else current_robo_santa["y"] - 1
            case "<":
                new_point["x"] = current_santa["x"] - \
                    1 if turn % 2 == 0 else current_robo_santa["x"] - 1

        if turn % 2 == 0:
            current_santa["x"] = new_point["x"]
            current_santa["y"] = new_point["y"]
        else:
            current_robo_santa["x"] = new_point["x"]
            current_robo_santa["y"] = new_point["y"]

        if new_point not in visited:
            visited.append(new_point)
    return len(visited)


if __name__ == "__main__":
    path = []

    with open("input.txt", "r") as f:
        while True:
            char = f.read(1)
            path.append(char)
            if not char:
                break
    print(find_houses(path))
