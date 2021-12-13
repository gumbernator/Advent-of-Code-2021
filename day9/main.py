from typing import List


def part1(cave: List[List[int]]):
    total_risk = 0
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            adjs = [[i - 1, j], [i, j - 1], [i, j + 1], [i + 1, j]]
            is_low = True
            for adj in adjs:
                if 0 <= adj[0] < len(cave) and 0 <= adj[1] < len(cave[i]):
                    if cave[i][j] >= cave[adj[0]][adj[1]]:
                        is_low = False
            if is_low:
                total_risk += 1 + cave[i][j]

    print("part 1:", total_risk)
    pass


def find_basin(cave: List[List[int]], i: int, j: int) -> int:
    adjs = [[i - 1, j], [i, j - 1], [i, j + 1], [i + 1, j]]
    size = 0
    for adj in adjs:
        if 0 <= adj[0] < len(cave) and 0 <= adj[1] < len(cave[i]):
            if cave[adj[0]][adj[1]] != -1 and cave[adj[0]][adj[1]] < 9:
                cave[adj[0]][adj[1]] = -1
                size += find_basin(cave, adj[0], adj[1]) + 1
    return size


def part2(cave: List[List[int]]):
    sizes = []
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            if cave[i][j] != -1 and cave[i][j] < 9:
                size = find_basin(cave, i, j)
                sizes.append(size)
    sizes.sort()

    print("part 2:", sizes[-1] * sizes[-2] * sizes[-3])
    pass


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in file.readlines()]
        matrix = []
        for line in input_lines:
            row = []
            for e in line:
                row.append(int(e))
            matrix.append(row)

        part1(matrix)
        part2(matrix)
