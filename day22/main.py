def part1(ins):
    on_cubes = set()

    for i in range(len(ins)):
        ins[i]['x_min'] = max(ins[i]['x_min'], -50)
        ins[i]['x_max'] = min(ins[i]['x_max'], 50)
        ins[i]['y_min'] = max(ins[i]['y_min'], -50)
        ins[i]['y_max'] = min(ins[i]['y_max'], 50)
        ins[i]['z_min'] = max(ins[i]['z_min'], -50)
        ins[i]['z_max'] = min(ins[i]['z_max'], 50)

        if ins[i]['on_off'] == 'on':
            for ii in range(ins[i]['x_min'], ins[i]['x_max'] + 1):
                for jj in range(ins[i]['y_min'], ins[i]['y_max'] + 1):
                    for kk in range(ins[i]['z_min'], ins[i]['z_max'] + 1):
                        on_cubes.add(f'{ii},{jj},{kk}')

        if ins[i]['on_off'] == 'off':
            for ii in range(ins[i]['x_min'], ins[i]['x_max'] + 1):
                for jj in range(ins[i]['y_min'], ins[i]['y_max'] + 1):
                    for kk in range(ins[i]['z_min'], ins[i]['z_max'] + 1):
                        if f'{ii},{jj},{kk}' in on_cubes:
                            on_cubes.remove(f'{ii},{jj},{kk}')
    print(len(on_cubes))


def part2():
    pass


if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        instructions = []

        for line in input_lines:
            on_off, dimensions = line.split(' ')
            x_dim, y_dim, z_dim = dimensions.split(',')
            x_min, x_max = x_dim.split('=')[1].split('..')
            y_min, y_max = y_dim.split('=')[1].split('..')
            z_min, z_max = z_dim.split('=')[1].split('..')
            instructions.append({
                'on_off': on_off,
                'x_min': int(x_min),
                'x_max': int(x_max),
                'y_min': int(y_min),
                'y_max': int(y_max),
                'z_min': int(z_min),
                'z_max': int(z_max),
            })

        part1(instructions)
        # print(instructions)
