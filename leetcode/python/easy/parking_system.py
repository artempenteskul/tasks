# task number - 1603


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int) -> None:
        self.parking = {
            1: big,
            2: medium,
            3: small
        }

    def add_car(self, car_type: int) -> bool:
        if car_type not in self.parking:
            raise ValueError('Unknown car type.')

        if self.parking[car_type] - 1 < 0:
            return False
        else:
            self.parking[car_type] -= 1
            return True


if __name__ == '__main__':
    parking_system = ParkingSystem(1, 1, 0)
    print(parking_system.add_car(1))  # true
    print(parking_system.add_car(2))  # true
    print(parking_system.add_car(3))  # false
    print(parking_system.add_car(1))  # false
