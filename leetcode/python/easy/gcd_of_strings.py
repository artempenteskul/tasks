# task number - 1071

def gcd_of_strings(str1: str, str2: str) -> str:
    shorter = str1 if len(str1) < len(str2) else str2
    len1, len2 = len(str1), len(str2)

    for l in range(len(shorter), 0, -1):
        if not len1 % l and not len2 % l:
            f1, f2 = len1 // l, len2 // l
            if shorter[:l] * f1 == str1 and shorter[:l] * f2 == str2:
                return shorter[:l]

    return ''


if __name__ == '__main__':
    input_str_1 = 'ABCABC'
    input_str_2 = 'ABC'
    print(f'GCD of input strings - "{gcd_of_strings(input_str_1, input_str_2)}"')  # "ABC"

    input_str_1 = 'ABABAB'
    input_str_2 = 'ABAB'
    print(f'GCD of input strings - "{gcd_of_strings(input_str_1, input_str_2)}"')  # "AB"

    input_str_1 = 'LEET'
    input_str_2 = 'CODE'
    print(f'GCD of input strings - "{gcd_of_strings(input_str_1, input_str_2)}"')  # ""
