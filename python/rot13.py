def rot13(message):
    res_message = ''
    for symbol in message:
        if 'a' <= symbol <= 'z':
            pos = ord(symbol) - ord('a')
            pos = (pos + 13) % 26
            coded_symbol = chr(pos + ord('a'))
            res_message += coded_symbol
        elif 'A' <= symbol <= 'Z':
            pos = ord(symbol) - ord('A')
            pos = (pos + 13) % 26
            coded_symbol = chr(pos + ord('A'))
            res_message += coded_symbol
        else:
            res_message += symbol
    return res_message


if __name__ == '__main__':
    users_message = input('Enter your message to code it by ROT13 algorithm: ')
    print(f'Your coded message: {rot13(users_message)}')
