# task number - 3110


def score_of_string(word: str) -> int:
    score = 0

    for index in range(len(word) - 1):
        score += abs(ord(word[index]) - ord(word[index + 1]))

    return score


if __name__ == '__main__':
    print(f'Score of word hello - {score_of_string(word="hello")}')  # 13
    print(f'Score of word zaz - {score_of_string(word="zaz")}')  # 50
