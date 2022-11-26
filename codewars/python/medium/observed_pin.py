NUM_VARIANTS = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9'],
    '0': ['8', '0']
}


def get_pins(observed):
    pins = []

    for num in observed:
        num_variants = NUM_VARIANTS[num]

        if len(pins) == 0:
            pins += num_variants
        else:
            old_pins = pins[:]
            pins = []

            for old_pin in old_pins:
                for num_variant in num_variants:
                    pins.append(old_pin + num_variant)

    return pins


if __name__ == '__main__':
    print(f'POSSIBLE PINS OF 8: {get_pins("8")}')  # ['5','7','8','9','0']
    print(f'POSSIBLE PINS OF 11: {get_pins("11")}')  # ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
