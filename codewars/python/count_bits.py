def count_bits(n: int):
    bit_n = bin(n)
    res = bit_n[2:]
    return sum(int(x) for x in res)


if __name__ == '__main__':
    users_num = int(input('Enter your number: '))
    print(f'Result for {users_num} = {count_bits(n=users_num)}')
