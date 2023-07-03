# task number - 58


def len_of_last_word(s: str) -> int:
    counter = 0

    for symbol in s[::-1]:
        if symbol != ' ':
            counter += 1
        else:
            if counter:
                break

    return counter


if __name__ == '__main__':
    print(len_of_last_word('Hello World'))  # 5
    print(len_of_last_word('   fly me   to   the moon  '))  # 4
    print(len_of_last_word('luffy is still joyboy'))  # 6
