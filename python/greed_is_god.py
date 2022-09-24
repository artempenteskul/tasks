# three 1 => 1000 points
# three 6 => 600 points
# three 5 => 500 points
# three 4 => 400 points
# three 3 => 300 points
# three 2 => 200 points
# one 1 => 100 points
# one 5 => 50 points


def score(dices_list: list):
    dices = dices_list[:]
    dices_score = 0

    def _delete_duplicates(value):
        for i in range(3):
            dices.remove(value)

    if dices.count(1) == 3:
        dices_score += 1000
        _delete_duplicates(1)

    if dices.count(6) == 3:
        dices_score += 600
        _delete_duplicates(6)

    if dices.count(5) == 3:
        dices_score += 500
        _delete_duplicates(5)

    if dices.count(4) == 3:
        dices_score += 400
        _delete_duplicates(4)

    if dices.count(3) == 3:
        dices_score += 300
        _delete_duplicates(3)

    if dices.count(2) == 3:
        dices_score += 200
        _delete_duplicates(2)

    rest_ones_score = dices.count(1) * 100
    rest_fives_score = dices.count(5) * 50
    dices_score += rest_ones_score + rest_fives_score
    return dices_score


if __name__ == '__main__':
    dices_to_count_score = [2, 3, 4, 6, 2]
    print(score(dices_to_count_score))
    dices_to_count_score_2 = [4, 4, 4, 3, 3]
    print(score(dices_to_count_score_2))
