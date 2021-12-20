from copy import deepcopy
from typing import List


def add_padding(img: List[List[str]], size: int, val: str):
    for _ in range(size):
        img.insert(0, [val] * len(img[0]))
        img.append([val] * len(img[0]))
        for i in range(len(img)):
            img[i].insert(0, val)
            img[i].append(val)


def solve(enh: str, img: List[List[str]], steps: int):
    add_padding(img, 2, '.')
    for _ in range(steps):
        border = img[0][0]
        add_padding(img, 1, border)
        new_img = deepcopy(img)
        for i in range(len(new_img[0])):
            if border == '.':
                new_img[0][i] = enh[0]
                new_img[-1][i] = enh[0]
            else:
                new_img[0][i] = enh[-1]
                new_img[-1][i] = enh[-1]

        for i in range(len(new_img)):
            if border == '.':
                new_img[i][0] = enh[0]
                new_img[i][-1] = enh[0]
            else:
                new_img[i][0] = enh[-1]
                new_img[i][-1] = enh[-1]

        for i in range(1, len(new_img) - 1):
            for j in range(1, len(new_img[0]) - 1):
                square = img[i - 1][j - 1:j + 2] + img[i][j - 1:j + 2] + img[i + 1][j - 1:j + 2]
                bin_str = ''
                for e in square:
                    bin_str += '0' if e == '.' else '1'
                idx = int(bin_str, 2)
                new_img[i][j] = enh[idx]
        img = new_img

    count = 0
    for row in img:
        count += row.count('#')
    print(count)


if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        enhancer = input_lines[0]

        image = []
        for ii in range(2, len(input_lines)):
            image.append(list(input_lines[ii]))

        solve(enhancer, image, 50)
