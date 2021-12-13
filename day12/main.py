from copy import deepcopy
from typing import List
import itertools


def find_paths(curr_cave: str, caves: dict) -> List[List[str]]:
    paths = []
    caves[curr_cave]['visited'] += 1
    for neighbour in caves[curr_cave]['neighbours']:
        if neighbour == 'end':
            paths.append([curr_cave, 'end'])
        elif caves[neighbour]['visited'] == 0 and neighbour.islower() or neighbour.isupper():
            for path in find_paths(neighbour, deepcopy(caves)):
                paths.append([curr_cave] + path)

    return paths


def part1(caves: dict):
    paths = find_paths('start', caves)
    print(len(paths))


def find_paths_2(curr_cave: str, caves: dict, special_cave: str) -> List[List[str]]:
    paths = []
    caves[curr_cave]['visited'] += 1
    for neighbour in caves[curr_cave]['neighbours']:
        if neighbour == 'end':
            paths.append([curr_cave, 'end'])
        elif caves[neighbour]['visited'] == 0 and neighbour.islower() and neighbour != special_cave or neighbour.isupper() or caves[neighbour]['visited'] < 2 and neighbour == special_cave:
            for path in find_paths_2(neighbour, deepcopy(caves), special_cave):
                paths.append([curr_cave] + path)

    return paths


def part2(caves: dict):
    small_caves = []
    for cave in caves.keys():
        if cave != 'start' and cave != 'end' and cave.islower():
            small_caves.append(cave)
    total_paths = []
    for small_cave in small_caves:
        possible_paths = find_paths_2('start', deepcopy(caves), small_cave)
        total_paths.extend(possible_paths)
    total_paths.sort()
    # new_total_paths = []
    new_total_paths = list(k for k, _ in itertools.groupby(total_paths))
    print(len(new_total_paths))


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]
        connections = [line.split('-') for line in input_lines]

        in_caves = {}
        for conn in connections:
            if conn[0] not in in_caves.keys():
                in_caves[conn[0]] = {'visited': 0, 'neighbours': [conn[1]]}
            else:
                in_caves[conn[0]]['neighbours'].append(conn[1])
            if conn[1] not in in_caves.keys():
                in_caves[conn[1]] = {'visited': 0, 'neighbours': [conn[0]]}
            else:
                in_caves[conn[1]]['neighbours'].append(conn[0])

        print(in_caves)
        part1(deepcopy(in_caves))
        part2(deepcopy(in_caves))
