grid_size = 1000
grid = [[0 for i in range(grid_size)] for j in range(grid_size)]


def light_lights(instruction):
    # get instructions
    command = instruction[0]
    start = instruction[1].split(",")
    start_x = int(start[0])
    start_y = int(start[1])
    end = instruction[3].split(",")
    end_x = int(end[0])
    end_y = int(end[1])

    i = start_y
    j = start_x

    while i <= end_y:
        while j <= end_x:
            match command:
                case "on":
                    grid[i][j] += 1
                case "off":
                    grid[i][j] -= 1 if grid[i][j] > 0 else 0
                case "toggle":
                    grid[i][j] += 2
            j += 1

        i += 1
        j = start_x


def get_count(instructions):
    for instruction in instructions:
        light_lights(instruction)
    return (sum(map(sum, grid)))


if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            instruction = line.strip().split(" ")
            if instruction[0] == "turn":
                instruction.remove(instruction[0])
            input.append(instruction)
    print(get_count(input))
