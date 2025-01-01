# task number - 1422
# topics - string, prefix sum


def max_score(s: str) -> int:
    score_max = 0
    score_left = 0
    score_right = s.count('1')

    for i in range(len(s) - 1):
        if s[i] == '0':
            score_left += 1

        if s[i] == '1':
            score_right -= 1

        score_max = max(score_max, score_left + score_right)

    return score_max


if __name__ == '__main__':
    input_s = '011101'
    print(f'Max score after input str split - {max_score(input_s)}')  # 5

    input_s = '00111'
    print(f'Max score after input str split - {max_score(input_s)}')  # 5

    input_s = '1111'
    print(f'Max score after input str split - {max_score(input_s)}')  # 3
