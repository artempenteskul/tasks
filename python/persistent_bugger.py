def persistence(number: int):
    if len(str(number)) == 1:
        return 0
    new_num = 1
    for x in str(number):
        new_num *= int(x)
    return 1 + persistence(new_num)


if __name__ == '__main__':
    print(persistence(number=39))
    print(persistence(number=999))
