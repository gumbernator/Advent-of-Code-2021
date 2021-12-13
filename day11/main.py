from copy import deepcopy
from typing import List


def pprint(cave: List[List[int]]):
    for row in cave:
        print(''.join(str(x) for x in row))
    print()


def flash(cave: List[List[int]], i: int, j: int):
    adjs = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1],
            [i, j + 1], [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]]
    for adj in adjs:
        if 0 <= adj[0] < len(cave) and 0 <= adj[1] < len(cave[0]):
            if cave[adj[0]][adj[1]] != 0:
                cave[adj[0]][adj[1]] += 1


def part1(cave: List[List[int]]):
    flash_count = 0
    for step in range(100):
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                cave[i][j] += 1

        flashes = []
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                if cave[i][j] > 9:
                    flashes.append([i, j])
                    cave[i][j] = 0

        while len(flashes) > 0:
            for pos in flashes:
                flash(cave, pos[0], pos[1])
                flash_count += 1
            flashes = []
            for i in range(len(cave)):
                for j in range(len(cave[i])):
                    if cave[i][j] > 9:
                        flashes.append([i, j])
                        cave[i][j] = 0

    print(flash_count)


def part2(cave: List[List[int]]):
    flash_count = 0
    step = 0
    while True:
        step += 1
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                cave[i][j] += 1

        flashes = []
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                if cave[i][j] > 9:
                    flashes.append([i, j])
                    cave[i][j] = 0

        while len(flashes) > 0:
            for pos in flashes:
                flash(cave, pos[0], pos[1])
                flash_count += 1
            flashes = []
            for i in range(len(cave)):
                for j in range(len(cave[i])):
                    if cave[i][j] > 9:
                        flashes.append([i, j])
                        cave[i][j] = 0

        s = sum([sum(row) for row in cave])
        if s == 0:
            print(step)
            return


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]
        grid = []
        for line in input_lines:
            grid.append([int(e) for e in line])

        part1(deepcopy(grid))
        part2(deepcopy(grid))
