from copy import deepcopy
from typing import List


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.horizontal = self.y1 == self.y2
        self.vertical = self.x1 == self.x2
        self.diagonal = False
        if not self.horizontal and not self.vertical:
            self.diagonal = True

    def __str__(self):
        return f'{self.x1} {self.y1} {self.x2} {self.y2} {self.horizontal} {self.vertical}'


def part1(lns: List[Line]):
    ocean = []
    for i in range(1000):
        ocean.append([0] * 1000)

    for line in lns:
        if line.vertical:
            min_y = min(line.y1, line.y2)
            max_y = max(line.y1, line.y2)
            for i in range(min_y, max_y + 1):
                ocean[i][line.x1] += 1
        elif line.horizontal:
            min_x = min(line.x1, line.x2)
            max_x = max(line.x1, line.x2)
            for i in range(min_x, max_x + 1):
                ocean[line.y1][i] += 1

    count = 0
    for row in ocean:
        for el in row:
            if el > 1:
                count += 1
    print(count)


def part2(lns: List[Line]):
    ocean = []
    for i in range(1000):
        ocean.append([0] * 1000)

    for line in lns:
        if line.vertical:
            min_y = min(line.y1, line.y2)
            max_y = max(line.y1, line.y2)
            for i in range(min_y, max_y + 1):
                ocean[i][line.x1] += 1
        elif line.horizontal:
            min_x = min(line.x1, line.x2)
            max_x = max(line.x1, line.x2)
            for i in range(min_x, max_x + 1):
                ocean[line.y1][i] += 1
        else:
            x_diff = line.x1 - line.x2
            y_diff = line.y1 - line.y2

            if x_diff > 0 and y_diff > 0:
                for i in range(abs(x_diff) + 1):
                    ocean[line.y1 - i][line.x1 - i] += 1
            elif x_diff > 0 and y_diff < 0:
                for i in range(abs(x_diff) + 1):
                    ocean[line.y1 + i][line.x1 - i] += 1
            elif x_diff < 0 and y_diff > 0:
                for i in range(abs(x_diff) + 1):
                    ocean[line.y1 - i][line.x1 + i] += 1
            elif x_diff < 0 and y_diff < 0:
                for i in range(abs(x_diff) + 1):
                    ocean[line.y1 + i][line.x1 + i] += 1

    count = 0
    for row in ocean:
        for el in row:
            if el > 1:
                count += 1
    print(count)


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        lines = []
        for input_line in input_lines:
            coordinates = input_line.split(' -> ')
            point1 = coordinates[0].split(',')
            point2 = coordinates[1].split(',')
            line = Line(int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1]))
            lines.append(line)

        part1(deepcopy(lines))
        part2(deepcopy(lines))
