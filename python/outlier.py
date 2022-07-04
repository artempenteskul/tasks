def find_outlier(integers: list):
    reminders = [x % 2 for x in integers]
    if reminders.count(1) == 1:
        return integers[reminders.index(1)]
    elif reminders.count(0) == 1:
        return integers[reminders.index(0)]
    else:
        return 'Your sequence has not outlier!'


if __name__ == '__main__':
    num = input('Enter the first num of the sequence or press enter to stop: ')
    nums = []
    while num != '':
        nums.append(int(num))
        num = input('Enter next num or press enter to stop: ')
    print('Finding outlier...')
    print(f'Result: {find_outlier(integers=nums)}')
