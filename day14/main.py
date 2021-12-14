from copy import copy
from typing import Dict


def part1(temp: str, rules: Dict[str, str]):
    for _ in range(10):
        insertions = []
        for i in range(len(temp) - 1):
            insertions.append(rules[temp[i:i+2]])

        new_temp = ''
        for i in range(len(temp)):
            new_temp += temp[i]
            if len(insertions) > 0:
                new_temp += insertions[0]
                del insertions[0]

        temp = new_temp

    char_set = set()
    for c in temp:
        char_set.add(c)
    max_occur = float('-inf')
    min_occur = float('inf')
    for c in char_set:
        count = temp.count(c)
        max_occur = max(max_occur, count)
        min_occur = min(min_occur, count)

    print(max_occur - min_occur)


def part2(temp: str, rules: Dict[str, str]):
    empty_combos = {}
    for key in rules.keys():
        empty_combos[key] = 0

    combos = copy(empty_combos)
    for i in range(len(temp) - 1):
        combos[temp[i:i+2]] += 1

    for step in range(40):
        new_combos = copy(empty_combos)
        for key in combos.keys():
            new_combos[key[0] + rules[key]] += combos[key]
            new_combos[rules[key] + key[1]] += combos[key]
        combos = new_combos

    char_counts = {}
    for key in combos.keys():
        for i in range(len(key)):
            if key[i] not in char_counts.keys():
                char_counts[key[i]] = combos[key]
            else:
                char_counts[key[i]] += combos[key]

    for char in char_counts.keys():
        if char_counts[char] % 2 == 0:
            char_counts[char] /= 2
        else:
            char_counts[char] += 1
            char_counts[char] /= 2
        char_counts[char] = int(char_counts[char])

    max_occur = max(list(char_counts.values()))
    min_occur = min(list(char_counts.values()))
    print(max_occur - min_occur)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        template = input_lines[0]
        ins_rules = {}
        for i in range(2, len(input_lines)):
            splits = input_lines[i].split(' -> ')
            ins_rules[splits[0]] = splits[1]

        part1(template, ins_rules)
        part2(template, ins_rules)
