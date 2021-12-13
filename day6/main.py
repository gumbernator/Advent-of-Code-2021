from copy import deepcopy
from typing import List


def part1(ages: List[int]):
    for i in range(0, 80):
        birth_count = 0
        for ii, num in enumerate(ages):
            if num == 0:
                ages[ii] = 6
                birth_count += 1
                continue
            ages[ii] -= 1
        for ii in range(0, birth_count):
            ages.append(8)
    print(len(ages))


def part2(ages: List[int]):
    age_groups = [0] * 9
    for age in ages:
        age_groups[age] += 1

    total_birth_count = 0
    for i in range(0, 256):
        print(age_groups)
        birth_count = 0
        for ii in range(0, 8):
            if ii == 0:
                birth_count = age_groups[ii]
            age_groups[ii] = age_groups[ii + 1]
        print(age_groups)

        age_groups[6] += birth_count
        age_groups[8] = birth_count
        total_birth_count += birth_count
        print(age_groups)
        print()

    print('total_birth_count', total_birth_count)
    print('total_birth_count + initial_poopulation', total_birth_count + len(ages))


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_line = file.readline()
        input_line = input_line.replace('\r\n', '').replace('\n', '')
        input_numbers = [int(e) for e in input_line.split(',')]

        # print(input_numbers)

        # part1(deepcopy(input_numbers))
        part2(deepcopy(input_numbers))
        # part2([3,4,3,1,2])
