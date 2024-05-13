# task number - 605


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True

    prev = 0

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            following = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            if prev == 0 and following == 0:
                flowerbed[i] = 1
                n -= 1

        prev = flowerbed[i]

    return n <= 0


if __name__ == '__main__':
    input_flowerbed = [1, 0, 0, 0, 1]
    input_n = 1
    print(f'Can place needed flowers quantity - {can_place_flowers(input_flowerbed, input_n)}')  # true

    input_flowerbed = [1, 0, 0, 0, 1]
    input_n = 2
    print(f'Can place needed flowers quantity - {can_place_flowers(input_flowerbed, input_n)}')  # false

    input_flowerbed = [1, 0, 0, 0, 0, 0, 1]
    input_n = 2
    print(f'Can place needed flowers quantity - {can_place_flowers(input_flowerbed, input_n)}')  # true

    input_flowerbed = [1, 0, 0, 0, 1, 0, 1]
    input_n = 1
    print(f'Can place needed flowers quantity - {can_place_flowers(input_flowerbed, input_n)}')  # true

    input_flowerbed = [1, 0, 0, 0, 1, 0, 0]
    input_n = 2
    print(f'Can place needed flowers quantity - {can_place_flowers(input_flowerbed, input_n)}')  # true
