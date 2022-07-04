def create_phone_number(nums):
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*nums)
    return phone_number


if __name__ == '__main__':
    users_nums = []
    for i in range(10):
        num = input(f'Enter int number {i + 1}: ')
        users_nums.append(num)
    print(f'Your phone number: {create_phone_number(users_nums)}')
