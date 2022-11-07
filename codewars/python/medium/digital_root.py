def digital_root(n):
    if len(str(n)) == 1:
        return n
    number = str(n)
    numbers = []
    for num in number:
        numbers.append(int(num))
    new_num = sum(numbers)
    return digital_root(new_num)


if __name__ == '__main__':
    users_number = int(input('Enter your number in order to get its digital root: '))
    print(f'Digital root of {users_number} is {digital_root(users_number)}')
