# task number - 13

LATIN_TO_INT = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
    'IV': 4, 'IX': 9,
    'XL': 40, 'XC': 90,
    'CD': 400, 'CM': 900
}


def roman_to_integer(latin: str) -> int:
    res = 0
    case = ''

    for symbol_index, symbol_value in enumerate(latin):
        if not case and symbol_value in ('I', 'X', 'C') and symbol_index + 1 < len(latin):
            if symbol_value == 'I' and latin[symbol_index + 1] in ('V', 'X'):
                case += 'I'
            elif symbol_value == 'X' and latin[symbol_index + 1] in ('L', 'C'):
                case += 'X'
            elif symbol_value == 'C' and latin[symbol_index + 1] in ('D', 'M'):
                case += 'C'
            else:
                res += LATIN_TO_INT[symbol_value]
        elif case and symbol_value in ('V', 'X', 'L', 'C', 'D', 'M'):
            case += symbol_value
            res += LATIN_TO_INT[case]
            case = ''
        else:
            res += LATIN_TO_INT[symbol_value]

    return res


def roman_to_integer_2(s: str) -> int:
    res = 0

    for i in range(len(s) - 1):
        if LATIN_TO_INT[s[i]] < LATIN_TO_INT[s[i + 1]]:
            res -= LATIN_TO_INT[s[i]]
        else:
            res += LATIN_TO_INT[s[i]]

    return res + LATIN_TO_INT[s[-1]]


if __name__ == '__main__':
    print(roman_to_integer('III'))  # 3
    print(roman_to_integer('LVIII'))  # 58
    print(roman_to_integer('MCMXCIV'))  # 1994
