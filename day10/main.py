from typing import List


def part1(lines: List[str]):
    corrupted = ''
    for line in lines:
        stack = []
        expecting = []
        for c in line:
            if c == '[':
                stack.append(c)
                expecting.append(']')
                continue
            elif c == '(':
                stack.append(c)
                expecting.append(')')
                continue
            elif c == '{':
                stack.append(c)
                expecting.append('}')
                continue
            elif c == '<':
                stack.append(c)
                expecting.append('>')
                continue
            if c == expecting[-1]:
                del expecting[-1]
            else:
                corrupted += c
                break

    print(corrupted)
    total_point = 0
    for corrupt in corrupted:
        if corrupt == ')':
            total_point += 3
        elif corrupt == ']':
            total_point += 57
        elif corrupt == '}':
            total_point += 1197
        elif corrupt == '>':
            total_point += 25137
    print(total_point)


def part2(lines: List[str]):
    expected_letters = []
    for line in lines:
        stack = []
        expecting = ''
        is_corrupted = False
        for c in line:
            if c == '[':
                stack.append(c)
                expecting += ']'
                continue
            elif c == '(':
                stack.append(c)
                expecting += ')'
                continue
            elif c == '{':
                stack.append(c)
                expecting += '}'
                continue
            elif c == '<':
                stack.append(c)
                expecting += '>'
                continue
            if c == expecting[-1]:
                expecting = expecting[:-1]
            else:
                is_corrupted = True
                break
        if not is_corrupted:
            expected_letters.append(expecting)

    print(expected_letters)
    points = []
    for expected_letter in expected_letters:
        point = 0
        for c in reversed(expected_letter):
            point *= 5
            if c == ')':
                point += 1
            elif c == ']':
                point += 2
            elif c == '}':
                point += 3
            elif c == '>':
                point += 4
        print(expected_letter, ":", point)
        points.append(point)
    points.sort()
    print(points)
    print(points[int(len(points) / 2)])


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]
        print(input_lines)

        part1(input_lines)
        part2(input_lines)
