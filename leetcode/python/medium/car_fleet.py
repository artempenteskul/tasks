# task number - 853
# topics - array, stack, sorting, monotonic stack


def car_fleets(target: int, position: list[int], speed: list[int]) -> int:
    pairs = sorted([(p, s) for p, s in zip(position, speed)], key=lambda x: x[0], reverse=True)

    fleets = 0
    max_time = 0

    for p, s in pairs:
        pos_time = (target - p) / s
        if pos_time > max_time:
            fleets += 1
            max_time = pos_time

    return fleets


if __name__ == '__main__':
    input_target = 12
    input_position = [10, 8, 0, 5, 3]
    input_speed = [2, 4, 1, 1, 3]
    print(f'Qty of car fleets for input - {car_fleets(input_target, input_position, input_speed)}')  # 3

    input_target = 10
    input_position = [3]
    input_speed = [3]
    print(f'Qty of car fleets for input - {car_fleets(input_target, input_position, input_speed)}')  # 1

    input_target = 100
    input_position = [0, 2, 4]
    input_speed = [4, 2, 1]
    print(f'Qty of car fleets for input - {car_fleets(input_target, input_position, input_speed)}')  # 1

    input_target = 20
    input_position = [6, 2, 17]
    input_speed = [3, 9, 2]
    print(f'Qty of car fleets for input - {car_fleets(input_target, input_position, input_speed)}')  # 2
