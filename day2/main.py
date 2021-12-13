def part1(lines):
    x, y = 0, 0
    for line in lines:
        movement, amount = line.split(' ')
        if movement == 'forward':
            x += int(amount)
        elif movement == 'down':
            y += int(amount)
        else:
            y -= int(amount)
    print(x * y)


def part2(lines):
    x, y, aim = 0, 0, 0
    for line in lines:
        movement, amount = line.split(' ')
        if movement == 'forward':
            x += int(amount)
            y += int(amount) * aim
        elif movement == 'down':
            aim += int(amount)
        else:
            aim -= int(amount)
    print(x * y)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        inputLines = file.readlines()
        part1(inputLines)
        part2(inputLines)
