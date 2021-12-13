from copy import copy
from typing import List


def split(grid: List[List[int]], direction: str, idx: int) -> (List, List):
    one, two = [], []

    if direction == 'y':
        return grid[:idx], grid[idx+1:]
        # one = copy(grid[:idx])
        # two = copy(grid[(idx+1):])
    elif direction == 'x':
        for row in grid:
            one.append([])
            two.append([])
            one[-1].extend(row[:idx])
            two[-1].extend(row[(idx+1):])

    return one, two


def inverse(grid: List[List[int]], direction: str):
    new_grid = []
    if direction == 'up':
        new_grid = grid[::-1]
    elif direction == 'left':
        new_grid = [row[::-1] for row in grid]
    return new_grid


def add(a: List[List[int]], b: List[List[int]], direction: str):
    new_grid = []
    if direction == 'y':
        a_iter = len(a) - 1
        b_iter = len(b) - 1
        while a_iter >= 0 and b_iter >= 0:
            new_line = []
            for i in range(len(a[0])):
                if a[a_iter][i] == '#' or b[b_iter][i] == '#':
                    new_line.append('#')
                else:
                    new_line.append('.')
            new_grid.append(new_line)
            a_iter -= 1
            b_iter -= 1

        while a_iter >= 0:
            new_grid.append(copy(a[a_iter]))
            a_iter -= 1

        while b_iter >= 0:
            new_grid.append(copy(b[b_iter]))
            b_iter -= 1
        return new_grid[::-1]
    elif direction == 'x':
        for ii in range(len(a)):
            new_line = []
            a_iter = 0
            b_iter = 0
            while a_iter < len(a[0]) and b_iter < len(b[0]):
                if a[ii][a_iter] == '#' or b[ii][b_iter] == '#':
                    new_line.append('#')
                else:
                    new_line.append('.')
                a_iter += 1
                b_iter += 1

            while a_iter < len(a[0]):
                new_line.append(a[ii][a_iter])
                a_iter += 1

            while b_iter < len(b[0]):
                new_line.append(b[ii][b_iter])
                b_iter += 1
            new_grid.append(new_line)
        return new_grid


def solve(coords: List[List[int]], folds: List[List]):
    height = max([e[0] for e in coords]) + 1
    width = max([e[1] for e in coords]) + 1

    grid = []
    for i in range(width):
        grid.append([])
        for j in range(height):
            grid[i].append('.')

    for coord in coords:
        grid[coord[1]][coord[0]] = '#'

    print()
    for i, fold in enumerate(folds):
        if fold[0] == 'x':
            one, two = split(grid, 'x', fold[1])
            one = inverse(one, 'left')
            grid = add(one, two, 'x')
        elif fold[0] == 'y':
            one, two = split(grid, 'y', fold[1])
            two = inverse(two, 'up')
            grid = add(one, two, 'y')
        count = 0
        for row in grid:
            count += row.count('#')
        print(f'#{i+1} fold: {count}')

    [print(l) for l in inverse(grid, 'left')]


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        coordinates = []
        for line in input_lines:
            if line == '':
                break
            coordinates.append([int(e) for e in line.split(',')])

        in_folds = []
        for line in input_lines:
            if line.startswith('fold'):
                in_fold = line.split(' ')[2].split('=')
                in_fold[1] = int(in_fold[1])
                in_folds.append(in_fold)

        solve(coordinates, in_folds)
