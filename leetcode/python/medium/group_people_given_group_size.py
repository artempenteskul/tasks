# task number - 1282


def group_the_people(group_sizes: list[int]) -> list[list[int]]:
    res_groups = []
    desired_groups = {}

    for i in range(len(group_sizes)):
        group_size = group_sizes[i]
        if group_size not in desired_groups:
            desired_groups[group_size] = [i]
        else:
            desired_groups[group_size].append(i)

        if len(desired_groups[group_size]) == group_size:
            res_groups.append(desired_groups[group_size])
            del desired_groups[group_size]

    return res_groups


if __name__ == '__main__':
    input_group_sizes = [3, 3, 3, 3, 3, 1, 3]
    print(f'Group the people for input {input_group_sizes} - {group_the_people(input_group_sizes)}')
    # [[5], [0, 1, 2], [3, 4, 6]]

    input_group_sizes = [2, 1, 3, 3, 3, 2]
    print(f'Group the people for input {input_group_sizes} - {group_the_people(input_group_sizes)}')
    # [[1], [0, 5], [2, 3, 4]]
