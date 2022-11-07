def make_readable(seconds: int):
    if seconds > 360000 or seconds < 0:
        return None
    hours = seconds // 3600
    rest_time = seconds % 3600
    minutes = rest_time // 60
    rest_time %= 60
    seconds = rest_time
    time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    return time


if __name__ == '__main__':
    users_seconds = int(input('Enter quantity of the seconds: '))
    print(f'Your time in readable format: {make_readable(seconds=users_seconds)}')
