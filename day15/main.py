from copy import copy
from typing import List
from dijkstar import Graph, find_path


def part1(cave: List[List[int]]):
    graph = Graph()
    for i in range(len(cave)):
        for j in range(len(cave[0])):
            adjs = [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]
            for adj in adjs:
                if 0 <= adj[0] < len(cave) and 0 <= adj[1] < len(cave[0]):
                    graph.add_edge(i * len(cave[0]) + j, adj[0] * len(cave[0]) + adj[1], cave[adj[0]][adj[1]])

    path = find_path(graph, 0, (len(cave) - 1) * len(cave[0]) + len(cave[0]) - 1)
    print(path)
    print(sum(path.edges))
    pass


def increment(e: int):
    if e == 9:
        return 1
    return e + 1


def part2(cave: List[List[int]]):
    for i, row in enumerate(cave):
        for _ in range(4):
            row = [increment(e) for e in row]
            cave[i].extend(row)

    new_cave = copy(cave)
    for _ in range(4):
        new_cave = [[increment(e) for e in row] for row in new_cave]
        cave.extend(new_cave)

    part1(cave)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        matrix = []
        for line in input_lines:
            matrix.append([int(e) for e in line])

        part1(matrix)
        part2(matrix)
