from copy import deepcopy

from typing import List


def check_for_win(brd, row_idx, col_idx):
    row_won = True
    for el in brd[row_idx]:
        if el != -1:
            row_won = False

    col_won = True
    for idx in range(len(brd)):
        if brd[idx][col_idx] != -1:
            col_won = False

    return row_won or col_won


def calculate_point(num, brd):
    unmarked_sum = 0
    for row in brd:
        for el in row:
            if el != -1:
                unmarked_sum += el
    return unmarked_sum * num


def part1(num_order: List[int], brds: List[List[List[int]]]):
    for num in num_order:
        for idx, brd in enumerate(brds):
            for i, row in enumerate(brd):
                for j, el in enumerate(row):
                    if el == num:
                        brds[idx][i][j] = -1
                        if check_for_win(brds[idx], i, j):
                            print(num, idx, brds[idx], calculate_point(num, brds[idx]))
                            return


def part2(num_order, brds):
    boards_won = [False] * len(brds)
    for num in num_order:
        for idx, brd in enumerate(brds):
            for i, row in enumerate(brd):
                for j, el in enumerate(row):
                    if el == num:
                        brds[idx][i][j] = -1
                        if not boards_won[idx]:
                            if boards_won.count(False) == 1:
                                print(num, idx, brds[idx], calculate_point(num, brds[idx]))
                                return
                            boards_won[idx] = check_for_win(brds[idx], i, j)


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        number_order = [int(n) for n in input_lines[0].split(',')]

        boards = []
        board = []
        for i in range(2, len(input_lines)):
            if input_lines[i] == '':
                boards.append(board)
                board = []
                continue
            board.append([int(n) for n in input_lines[i].strip().split(' ') if n.strip() != ''])
        boards.append(board)

        part1(number_order, deepcopy(boards))
        part2(number_order, deepcopy(boards))
