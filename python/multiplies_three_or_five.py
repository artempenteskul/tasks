def three_or_five_multiplies(number):
    numbers = []
    if number <= 0:
        return 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
    return sum(numbers)


if __name__ == '__main__':
    users_number = int(input('Enter limit number: '))
    print(f'The sum of your multiplies: {three_or_five_multiplies(users_number)}')
