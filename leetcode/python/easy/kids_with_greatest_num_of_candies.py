# task number - 1431


def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies = max(candies)
    return [x + extra_candies >= max_candies for x in candies]


if __name__ == '__main__':
    input_candies = [2, 3, 5, 1, 3]
    input_extra_candies = 3
    print(f'Output of kids with greatest num of candies - {kids_with_candies(input_candies, input_extra_candies)}')
    # [true, true, true, false, true]

    input_candies = [4, 2, 1, 1, 2]
    input_extra_candies = 1
    print(f'Output of kids with greatest num of candies - {kids_with_candies(input_candies, input_extra_candies)}')
    # [true, false, false, false, false]

    input_candies = [12, 1, 12]
    input_extra_candies = 10
    print(f'Output of kids with greatest num of candies - {kids_with_candies(input_candies, input_extra_candies)}')
    # [true, false, true]
