def part1():
    pass


def part2():
    pass


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        x_target = set(list(range(156, 203)))
        y_target = set(list(range(-110, -68)))
        # x_target = set(list(range(20, 31)))
        # y_target = set(list(range(-10, -4)))
        solutions = []

        for vx in range(1, 250):
            for vy in range(-110, 1000):
                x, y = 0, 0
                vx0, vy0 = vx, vy
                for t in range(1, 300):
                    x += vx0
                    y += vy0
                    vx0 -= 1 if vx0 != 0 else 0
                    vy0 -= 1
                    if x in x_target and y in y_target and [vx, vy] not in solutions:
                        print('found', vx, vy)
                        solutions.append([vx, vy])
                        print(len(solutions))


        # v = 19
        # x = 0
        # for t in range(1, 21):
        #     x += v
        #     v -= 1
        #     print(t, x, v)

        # y_target = set(list(range(-110, -68)))
        # for vy_iter in range(10, 1000):
        #     print(vy_iter)
        #     vy = vy_iter
        #     y = 0
        #     max_y = float('-inf')
        #     for t in range(1, 10000):
        #         y += vy
        #         vy -= 1
        #         max_y = max(max_y, y)
        #         if y in y_target:
        #             print('found!', max_y)
        #             break
        #         if y < -110:
        #             print('overshot!')
        #             break
