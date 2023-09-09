import numpy as np
import re


def find_signal(signal, wires, input):
    if signal in wires:
        return np.uint16(wires[signal])
    r = re.compile(rf".+->\W{signal}\b")
    signal_line = list(filter(r.match, input))[0].split()

    if len(signal_line) == 3:
        first = signal_line[0]
        if first.isdigit():
            wires[signal] = np.uint16(first)
        else:
            wires[signal] = find_signal(first, wires, input)
    elif len(signal_line) == 4:
        wires[signal] = ~find_signal(signal_line[1], wires, input)
    elif len(signal_line) == 5:
        match signal_line[1]:
            case "AND":
                if signal_line[0].isdigit():
                    wires[signal] = int(signal_line[0]) & find_signal(
                        signal_line[2], wires, input)
                else:
                    wires[signal] = find_signal(signal_line[0], wires, input) & find_signal(
                        signal_line[2], wires, input)
            case "OR":
                wires[signal] = find_signal(signal_line[0], wires, input) | find_signal(
                    signal_line[2], wires, input)
            case "LSHIFT":
                wires[signal] = find_signal(
                    signal_line[0], wires, input) << int(signal_line[2])
            case "RSHIFT":
                wires[signal] = find_signal(
                    signal_line[0], wires, input) >> int(signal_line[2])
    return np.uint16(wires[signal])


if __name__ == "__main__":
    wires = {'b': np.uint16(956)}
    input = []

    with open("input.txt", "r") as f:

        for line in f.readlines():
            input.append(line.strip())

    print(find_signal("a", wires, input))
