from typing import List


def parse(idx: int, message: str, versions: List[int]):
    if message[idx:].count('1') == 0:
        return
    version = int(message[idx:idx + 3], 2)
    versions.append(version)
    type_id = int(message[idx + 3:idx + 6], 2)

    if type_id == 4:
        group_idx = idx + 6
        value = ''
        while message[group_idx] != '0':
            value += message[group_idx + 1:group_idx + 5]
            group_idx += 5
        value += message[group_idx + 1:group_idx + 5]
        value = int(value, 2)
        return group_idx + 5
    else:
        length_type_id = int(message[idx + 6], 2)
        if length_type_id == 0:
            total_length = int(message[idx + 7:idx + 22], 2)
            current_idx = parse(idx + 22, message, versions)
            while current_idx != idx + 22 + total_length:
                current_idx = parse(current_idx, message, versions)
        else:
            sub_packet_num = int(message[idx + 7:idx + 18], 2)
            current_idx = idx + 18
            for _ in range(sub_packet_num):
                current_idx = parse(current_idx, message, versions)
        return current_idx


def parse_value(idx: int, message: str) -> (int, int):
    if message[idx:].count('1') == 0:
        return
    version = int(message[idx:idx + 3], 2)
    type_id = int(message[idx + 3:idx + 6], 2)

    if type_id == 4:
        group_idx = idx + 6
        value = ''
        while message[group_idx] != '0':
            value += message[group_idx + 1:group_idx + 5]
            group_idx += 5
        value += message[group_idx + 1:group_idx + 5]
        value = int(value, 2)
        return value, group_idx + 5
    else:
        packet_values = []
        length_type_id = int(message[idx + 6], 2)
        if length_type_id == 0:
            total_length = int(message[idx + 7:idx + 22], 2)
            value, current_idx = parse_value(idx + 22, message)
            packet_values.append(value)
            while current_idx != idx + 22 + total_length:
                value, current_idx = parse_value(current_idx, message)
                packet_values.append(value)
        else:
            sub_packet_num = int(message[idx + 7:idx + 18], 2)
            current_idx = idx + 18
            for _ in range(sub_packet_num):
                value, current_idx = parse_value(current_idx, message)
                packet_values.append(value)

        if type_id == 0:
            value = sum(packet_values)
        elif type_id == 1:
            value = 1
            for val in packet_values:
                value *= val
        elif type_id == 2:
            value = min(packet_values)
        elif type_id == 3:
            value = max(packet_values)
        elif type_id == 5:
            value = 1 if packet_values[0] > packet_values[1] else 0
        elif type_id == 6:
            value = 1 if packet_values[0] < packet_values[1] else 0
        elif type_id == 7:
            value = 1 if packet_values[0] == packet_values[1] else 0

        return value, current_idx


def part1(binary: str):
    vers = []
    parse(0, binary, vers)
    print(sum(vers))


def part2(binary: str):
    value, idx = parse_value(0, binary)
    print(value)


def hex_to_bin(hexadecimal: str):
    hexadecimal_to_binary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    binary = ''
    for c in hexadecimal:
        binary += hexadecimal_to_binary[c]

    return binary


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        input_binary = hex_to_bin(input_lines[0])

        part1(input_binary)
        part2(input_binary)
