# array A (first parameter) - durability of the rope
# array B (second parameter) - weight, connected to the rope
# array C (third parameter) - position to which we attach the rope - it could be -1 (means ceiling)


def solution(durability, weight, position):
    ropes = {}

    for i in range(len(durability)):
        rope_durability = durability[i]
        rope_weight = weight[i]
        rope_position = position[i]

        if rope_position == -1:
            parents = []
        else:
            parents = [rope_position] + ropes[rope_position][2]

        for parent in parents:
            parent_durability = ropes[parent][0]
            parent_weight = ropes[parent][1]
            if parent_weight + rope_weight > parent_durability:
                return len(ropes)
            else:
                ropes[parent][1] = parent_weight + rope_weight

        ropes[i] = [rope_durability, rope_weight, parents]


if __name__ == '__main__':
    A = [5, 3, 6, 3, 3]
    B = [2, 3, 1, 1, 2]
    C = [-1, 0, -1, 0, 3]
    print(solution(durability=A, weight=B, position=C))

    A1 = [4, 3, 1]
    B1 = [2, 2, 1]
    C1 = [-1, 0, 1]
    print(solution(durability=A1, weight=B1, position=C1))
