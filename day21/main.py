from typing import List


def landing_pos(start_pos: int, steps: int):
    final = (start_pos + steps) % 10
    return 10 if final == 0 else final


def find_win_count(p1_pos: int, p2_pos: int, p1_score: int, p2_score: int, turn: int) -> List[int]:
    if p1_score >= 21:
        return [1, 0]
    elif p2_score >= 21:
        return [0, 1]

    win_count = [0, 0]

    if turn == 1:
        land = landing_pos(p1_pos, 3)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 1
        win_count[1] += sub_count[1] * 1

        land = landing_pos(p1_pos, 4)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 3
        win_count[1] += sub_count[1] * 3

        land = landing_pos(p1_pos, 5)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 6
        win_count[1] += sub_count[1] * 6

        land = landing_pos(p1_pos, 6)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 7
        win_count[1] += sub_count[1] * 7

        land = landing_pos(p1_pos, 7)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 6
        win_count[1] += sub_count[1] * 6

        land = landing_pos(p1_pos, 8)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 3
        win_count[1] += sub_count[1] * 3

        land = landing_pos(p1_pos, 9)
        sub_count = find_win_count(land, p2_pos, p1_score + land, p2_score, 2)
        win_count[0] += sub_count[0] * 1
        win_count[1] += sub_count[1] * 1
    elif turn == 2:
        land = landing_pos(p2_pos, 3)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 1
        win_count[1] += sub_count[1] * 1

        land = landing_pos(p2_pos, 4)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 3
        win_count[1] += sub_count[1] * 3

        land = landing_pos(p2_pos, 5)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 6
        win_count[1] += sub_count[1] * 6

        land = landing_pos(p2_pos, 6)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 7
        win_count[1] += sub_count[1] * 7

        land = landing_pos(p2_pos, 7)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 6
        win_count[1] += sub_count[1] * 6

        land = landing_pos(p2_pos, 8)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 3
        win_count[1] += sub_count[1] * 3

        land = landing_pos(p2_pos, 9)
        sub_count = find_win_count(p1_pos, land, p1_score, p2_score + land, 1)
        win_count[0] += sub_count[0] * 1
        win_count[1] += sub_count[1] * 1
    return win_count


def part1(player1_pos: int, player2_pos: int):
    dice = 1

    player1_score = 0
    player2_score = 0

    turn = 1
    die_rolled = 0
    while player1_score < 1000 and player2_score < 1000:
        if turn == 1:
            player1_pos = landing_pos(player1_pos, 3 * dice + 3)
            player1_score += player1_pos
            die_rolled += 3
            dice += 3
            turn = 2
            continue
        elif turn == 2:
            player2_pos = landing_pos(player2_pos, 3 * dice + 3)
            player2_score += player2_pos
            die_rolled += 3
            dice += 3
            turn = 1
            continue

    print(player1_score, player2_score, die_rolled)
    if player1_score > player2_score:
        print(player2_score * die_rolled)
    else:
        print(player1_score * die_rolled)

    pass


if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        input_lines = file.readlines()
        input_lines = [line.replace('\r\n', '').replace('\n', '') for line in input_lines]

        part1(6, 2)
        rec = find_win_count(6, 2, 0, 0, 1)
        print(rec)
