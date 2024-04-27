# task number - 1672


def max_wealth(accounts: list[list[int]]) -> int:
    return max(sum(account) for account in accounts)


if __name__ == '__main__':
    input_accounts = [[1, 2, 3], [3, 2, 1]]
    print(f'Maximum wealth for the input accounts - {max_wealth(input_accounts)}')  # 6

    input_accounts = [[1, 5], [7, 3], [3, 5]]
    print(f'Maximum wealth for the input accounts - {max_wealth(input_accounts)}')  # 10
