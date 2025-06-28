# task number - 17
# topics - hash table, string, backtracking


def letter_combinations(digits: str) -> list[str]:
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    res = []

    if not digits:
        return res

    def backtrack(pos: int, current: str) -> None:
        if len(current) == len(digits):
            res.append(current)
            return

        for letter in phone[digits[pos]]:
            backtrack(pos + 1, current + letter)

    backtrack(0, '')

    return res


if __name__ == '__main__':
    input_digits = '23'
    print(f'Letter combinations - {letter_combinations(input_digits)}')  # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    input_digits = ''
    print(f'Letter combinations - {letter_combinations(input_digits)}')  # []

    input_digits = '2'
    print(f'Letter combinations - {letter_combinations(input_digits)}')  # ['a', 'b', 'c']
