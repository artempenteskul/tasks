# task number - 12
# topics - hash table, math, string


MAPPING = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
    90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
    9: 'IX', 5: 'V', 4: 'IV', 1: 'I',
}


def integer_to_roman(num: int) -> str:
    roman = ''

    for key, value in MAPPING.items():
        while num >= key:
            roman += value
            num -= key

    return roman


if __name__ == '__main__':
    input_num = 3749
    print(f'Result of integer {input_num} is Roman number - {integer_to_roman(input_num)}')  # 'MMMDCCXLIX'

    input_num = 58
    print(f'Result of integer {input_num} is Roman number - {integer_to_roman(input_num)}')  # 'LVIII'

    input_num = 1994
    print(f'Result of integer {input_num} is Roman number - {integer_to_roman(input_num)}')  # 'MCMXCIV'
