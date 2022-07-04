def rgb_to_hex(r: int, g: int, b: int):

    if r < 0:
        red = '0' * 2
    elif r > 255:
        red = 'F' * 2
    else:
        red = ('%02x' % r).upper()

    if g < 0:
        green = '0' * 2
    elif g > 255:
        green = 'F' * 2
    else:
        green = ('%02x' % g).upper()

    if b < 0:
        blue = '0' * 2
    elif b > 255:
        blue = 'F' * 2
    else:
        blue = ('%02x' % b).upper()

    return f'{red}{green}{blue}'


if __name__ == '__main__':
    print(rgb_to_hex(-20, 275, 125))
    print(rgb_to_hex(0, 0, 0))
    print(rgb_to_hex(133, 78, 222))
    print(rgb_to_hex(1, 2, 3))
