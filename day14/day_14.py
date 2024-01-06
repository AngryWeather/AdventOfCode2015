if __name__ == "__main__":
    input = []

    with open("input.txt") as f:
        for line in f.readlines():
            input.append(line)

    distance = {}

    seconds = 0
    reindeers = {}
    reindeer_counter = {}
    scores = {}

    for i in input:
        i = i.split()
        reindeers[i[0]] = [int(i[3]), int(i[6]), int(i[13]), False]
        reindeer_counter[i[0]] = [int(i[6]), int(i[13])]

    while seconds < 2503:
        for k, v in reindeers.items():
            if not v[3]:
                if k not in distance:
                    distance[k] = 0
                    distance[k] += v[0]
                else:
                    distance[k] += v[0]
                reindeer_counter[k][0] -= 1
                if reindeer_counter[k][0] == 0:
                    reindeers[k][3] = True
                    reindeer_counter[k][1] = reindeers[k][2]
            else:
                reindeer_counter[k][1] -= 1
                if reindeer_counter[k][1] == 0:
                    reindeers[k][3] = False
                    reindeer_counter[k][0] = reindeers[k][1]

        seconds += 1
        current_max = max(distance.values())
        d = [k for k, v in distance.items() if v == current_max]

        for r in d:
            if r not in scores:
                scores[r] = 0
                scores[r] += 1
            else:
                scores[r] += 1

    print(max(scores.values()))
