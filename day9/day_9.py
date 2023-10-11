import sys
from itertools import permutations


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight
        nbr.connected_to[self] = weight

    def get_connections(self):
        return self.connected_to

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.values()

    # def __iter__(self):
    #     return iter(self.vert_list.values())


g = Graph()


def dijkstra(aGraph, start):
    unvisited_nodes = list(aGraph.get_vertices())

    shortest_path = {}

    previous_nodes = {}

    max_value = sys.maxsize

    for node in unvisited_nodes:
        shortest_path[node] = max_value

    shortest_path[start] = 0

    while unvisited_nodes:
        # find node with the lowest distance
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = current_min_node.connected_to
        for neighbor in neighbors:
            val = shortest_path[current_min_node] + \
                current_min_node.get_weight(neighbor)
            if val < shortest_path[neighbor]:
                shortest_path[neighbor] = val
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path


def print_results(previous_nodes, shortest_path, start, target):
    path = []
    node = target

    while node != start:
        path.append(node)
        node = previous_nodes[node]

    path.append(start)

    # print("We found the following best path with a value of {}.".format(
    #     shortest_path[target]))
    # for p in path:
    #     print(p.get_id())
    return shortest_path[target]


if __name__ == "__main__":
    input = []

    with open("input.txt", "r") as f:
        for line in f.readlines():
            input.append(line.strip().split())

    g = Graph()

    for i in input:
        g.add_edge(i[0], i[2], int(i[4]))

    node_names = [node_name.get_id() for node_name in g.get_vertices()]

    perms = list(permutations(node_names))
    max_distance = 0

    distances = []
    for perm in perms:
        current_distance = 0
        for i, j in enumerate(perm):
            if i < len(perm) - 1:
                previous_nodes, shortest_path = dijkstra(g, g.get_vertex(j))
                current_distance += print_results(previous_nodes, shortest_path,
                                                  g.get_vertex(j), g.get_vertex(perm[i+1]))
        distances.append(current_distance)
        # print(distances)
        max_distance = max(distances)

    print("max: ", max_distance)
