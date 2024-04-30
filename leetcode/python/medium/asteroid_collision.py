# task number - 735


def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []

    for asteroid in asteroids:

        while stack and asteroid < 0 < stack[-1]:

            if abs(asteroid) > stack[-1]:
                stack.pop()

            elif abs(asteroid) == stack[-1]:
                stack.pop()
                break

            else:
                break

        else:
            stack.append(asteroid)

    return stack


if __name__ == '__main__':
    input_asteroids = [5, 10, -5]
    print(f'Result of input asteroid collision: {asteroid_collision(input_asteroids)}')  # [5, 10]

    input_asteroids = [8, -8]
    print(f'Result of input asteroid collision: {asteroid_collision(input_asteroids)}')  # []

    input_asteroids = [10, 2, -5]
    print(f'Result of input asteroid collision: {asteroid_collision(input_asteroids)}')  # [10]

    input_asteroids = [-2, -1, 1, 2]
    print(f'Result of input asteroid collision: {asteroid_collision(input_asteroids)}')  # [-2, -1, 1, 2]
