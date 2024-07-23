# task number - 2469


def convert_temperatures(celsius: float) -> list[float]:
    kelvins = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32
    return [kelvins, fahrenheit]


if __name__ == '__main__':
    input_celsius = 36.50
    print(f'Output temperatures - {convert_temperatures(input_celsius)}')  # [309.65000, 97.70000]

    input_celsius = 122.11
    print(f'Output temperatures - {convert_temperatures(input_celsius)}')  # [395.26000, 251.79800]
