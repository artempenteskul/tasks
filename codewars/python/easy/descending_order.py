def descending_order(num):
    num_list = [int(x) for x in str(num)]
    num_list.sort(reverse=True)
    str_list = [str(x) for x in num_list]
    return int(''.join(str_list))


if __name__ == '__main__':
    number = 15
    print(descending_order(number))
