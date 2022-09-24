def persistence(num: int, counter=0):
    if num < 10:
        return counter

    str_num = str(num)
    new_num = 1
    for n in str_num:
        new_num *= int(n)

    return persistence(new_num, counter=counter+1)


if __name__ == '__main__':
    number = 999
    print(persistence(number))
