from copy import copy
from typing import List


class Pair:
    def __init__(self, s: str, idx: List[int]):
        s = s[1:-1]
        if '[' not in s:
            splits = s.split(',')
            self.left = int(splits[0])
            self.right = int(splits[1])
            self.left_idx = idx[0] + 1
            idx[0] += 1
            self.right_idx = idx[0] + 1
            idx[0] += 1
            return

        depth = 0
        self.left = ''
        for c in s:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            self.left += c
            if depth == 0 and c == ',':
                break
        self.left = self.left[:-1]
        self.right = s.replace(self.left + ',', '', 1)

        if self.left.isnumeric():
            self.left = int(self.left)
            self.left_idx = idx[0] + 1
            idx[0] += 1
        else:
            self.left = Pair(self.left, idx)
            self.left_idx = None
        if self.right.isnumeric():
            self.right = int(self.right)
            self.right_idx = idx[0] + 1
            idx[0] += 1
        else:
            self.right = Pair(self.right, idx)
            self.right_idx = None

    def __str__(self):
        return f'[{self.left},{self.right}]'


def exploding_pair(snail_num: Pair, depth=0):
    if depth == 4:
        return snail_num
    if isinstance(snail_num.left, Pair):
        res = exploding_pair(snail_num.left, depth + 1)
        if res is not None:
            return res
    if isinstance(snail_num.right, Pair):
        res = exploding_pair(snail_num.right, depth + 1)
        if res is not None:
            return res
    return None


def add_to_pair(root: Pair, idx: int, val: int):
    if isinstance(root, int):
        return
    if root.left_idx == idx:
        root.left += val
    elif root.right_idx == idx:
        root.right += val
    add_to_pair(root.left, idx, val)
    add_to_pair(root.right, idx, val)


def set_zero(root: Pair, exploded_pair: Pair):
    if isinstance(root, int):
        return
    if root.left == exploded_pair:
        root.left = 0
        return
    if root.right == exploded_pair:
        root.right = 0
        return
    set_zero(root.left, exploded_pair)
    set_zero(root.right, exploded_pair)


def explode(snail_num: Pair):
    explode_pair = exploding_pair(snail_num)
    if explode_pair is None:
        return False
    print('explode_pair', explode_pair)
    add_to_pair(snail_num, explode_pair.left_idx - 1, explode_pair.left)
    add_to_pair(snail_num, explode_pair.right_idx + 1, explode_pair.right)
    set_zero(snail_num, explode_pair)
    return True


def splitting_idx(snail_num: Pair):
    if isinstance(snail_num, int):
        return None
    if isinstance(snail_num.left, int):
        if snail_num.left > 9:
            return snail_num.left_idx
    if isinstance(snail_num.right, int):
        if snail_num.right > 9:
            return snail_num.right_idx

    res = splitting_idx(snail_num.left)
    if res is not None:
        return res
    res = splitting_idx(snail_num.right)
    if res is not None:
        return res
    return None


def split_by_idx(snail_num: Pair, idx: int):
    if isinstance(snail_num, int):
        return
    if isinstance(snail_num.left, int):
        if snail_num.left_idx == idx:
            val = snail_num.left
            left = int(val / 2)
            right = int(val / 2) if val % 2 == 0 else int(val / 2) + 1
            snail_num.left = Pair(f'[{left},{right}]', [snail_num.left_idx - 1])
            return
    if isinstance(snail_num.right, int):
        if snail_num.right_idx == idx:
            val = snail_num.right
            left = int(val / 2)
            right = int(val / 2) if val % 2 == 0 else int(val / 2) + 1
            snail_num.right = Pair(f'[{left},{right}]', [snail_num.right_idx - 1])
            return
    split_by_idx(snail_num.left, idx)
    split_by_idx(snail_num.right, idx)


def split(snail_num: Pair):
    split_idx = splitting_idx(snail_num)
    if split_idx is None:
        return False
    print('split_idx', split_idx)
    split_by_idx(snail_num, split_idx)
    return True


def reduce(snail_num: Pair):
    new_snail_num = copy(snail_num)
    while True:
        if explode(new_snail_num):
            print('after explode', new_snail_num)
            new_snail_num = Pair(str(new_snail_num), [0])
            continue
        if split(new_snail_num):
            print('after split', new_snail_num)
            new_snail_num = Pair(str(new_snail_num), [0])
            continue
        break
    return new_snail_num


def add(snail_num1: Pair, snail_num2: Pair):
    return reduce(Pair(f'[{snail_num1},{snail_num2}]', [0]))


def magnitude(snail_num):
    pass


def part1(snail_nums: List[Pair]):
    res = snail_nums[0]
    print(Pair(f'[{snail_nums[0]},{snail_nums[1]}]', [0]))
    for i in range(1, len(snail_nums)):
        res = add(res, snail_nums[i])
        print(res)
    pass


def part2():
    pass


if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        input_pairs = []
        for line in input_lines:
            input_pairs.append(Pair(line, [0]))

        part1(input_pairs)
