# task number - 888


def fair_candy_swap(alice_sizes: list[int], bob_sizes: list[int]) -> list[int]:
    alice_total = sum(alice_sizes)
    bob_total = sum(bob_sizes)

    bob_sizes_set = set(bob_sizes)

    delta = (bob_total - alice_total) // 2

    for alice_size in alice_sizes:
        if alice_size + delta in bob_sizes_set:
            return [alice_size, alice_size + delta]

    return []


if __name__ == '__main__':
    print(fair_candy_swap(alice_sizes=[1, 1], bob_sizes=[2, 2]))  # [1, 2]
    print(fair_candy_swap(alice_sizes=[1, 2], bob_sizes=[2, 3]))  # [1, 2]
    print(fair_candy_swap(alice_sizes=[2], bob_sizes=[1, 3]))  # [2, 3]
    print(fair_candy_swap(alice_sizes=[1, 2, 5], bob_sizes=[2, 4]))  # [5, 4]
