def alphabet_position(text: str):
    indexes = [str((ord(x.lower()) - 96) % 27) for x in text if x.isalpha()]
    return ' '.join(indexes)


if __name__ == '__main__':
    users_text = input('Enter your text: ')
    print(f'Result: {alphabet_position(text=users_text)}')
