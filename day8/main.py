from typing import List


def all_perms(elements):
    if len(elements) <= 1:
        return elements
    else:
        tmp = set()
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.add(perm[:i] + elements[0:1] + perm[i:])
        return tmp


def overlap_count(str1, str2):
    count = 0
    for c1 in str1:
        for c2 in str2:
            if c1 == c2:
                count += 1
    return count


def get_codes(segments: List[str]):
    seg2num = {}
    num2seg = {}
    for seg in segments:
        if len(seg) == 2:
            seg2num[seg] = 1
            num2seg[1] = seg
        elif len(seg) == 3:
            seg2num[seg] = 7
            num2seg[7] = seg
        elif len(seg) == 4:
            seg2num[seg] = 4
            num2seg[4] = seg
        elif len(seg) == 7:
            seg2num[seg] = 8
            num2seg[8] = seg

    for seg in segments:
        if len(seg) == 6:
            if overlap_count(seg, num2seg[1]) == 1:
                seg2num[seg] = 6
                num2seg[6] = seg
            elif overlap_count(seg, num2seg[4]) == 3:
                seg2num[seg] = 0
                num2seg[0] = seg
            else:
                seg2num[seg] = 9
                num2seg[9] = seg

    for c1 in num2seg[1]:
        for csix in num2seg[6]:
            if c1 == csix:
                bottom_right = c1
                for seg in segments:
                    if len(seg) == 5:
                        if overlap_count(seg, num2seg[1]) == 2:
                            seg2num[seg] = 3
                            num2seg[3] = seg
                        elif bottom_right not in seg:
                            seg2num[seg] = 2
                            num2seg[2] = seg
                        else:
                            seg2num[seg] = 5
                            num2seg[5] = seg
    for seg in segments:
        seg_perms = all_perms(seg)
        for perm in seg_perms:
            seg2num[perm] = seg2num[seg]
    return seg2num


def part1(parts: List[str]):
    count = 0
    for part in parts:
        for segment in part.split(' '):
            length = len(segment)
            if length == 2 or length == 4 or length == 3 or length == 7:
                count += 1
    print(count)


def part2(f_parts: List[str], l_parts: List[str]):
    s = 0
    for i, f_part in enumerate(f_parts):
        codes = get_codes(f_part.split(' '))
        print(codes)
        out = ''
        for l_part in l_parts[i].split(' '):
            print(l_part)
            out += str(codes[l_part])
        s += int(out)
    print(s)


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [input_line.replace('\r\n', '').replace('\n', '') for input_line in input_lines]

        first_parts = [li.split(' | ')[0] for li in input_lines]
        second_parts = [li.split(' | ')[1] for li in input_lines]

        part1(second_parts)
        part2(first_parts, second_parts)
        # part2(
        #     [
        #         'fdgacbe cefdb cefbgd gcbe',
        #         'fcgedb cgb dgebacf gc',
        #         'cg cg fdcagb cbg',
        #         'efabcd cedba gadfec cb',
        #         'gecf egdcabf bgf bfgea',
        #         'gebdcfa ecba ca fadegcb',
        #         'cefg dcbef fcge gbcadfe',
        #         'ed bcgafe cdgba cbgef',
        #         'gbdfcae bgc cg cgb',
        #         'fgae cfgab fg bagce'
        #     ]
        # )
