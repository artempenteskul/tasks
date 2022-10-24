opposite = {
    'NORTH': 'SOUTH',
    'SOUTH': 'NORTH',
    'WEST': 'EAST',
    'EAST': 'WEST',
}


def direction_reduction(plan: list):
    new_plan = []
    for direction in plan:
        if new_plan and new_plan[-1] == opposite[direction]:
            new_plan.pop()
        else:
            new_plan.append(direction)
    return new_plan


if __name__ == '__main__':
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # should give ['WEST']
    print(direction_reduction(a))
    b = ["NORTH", "WEST", "SOUTH", "EAST"]  # should give ["NORTH", "WEST", "SOUTH", "EAST"]
    print(direction_reduction(b))
