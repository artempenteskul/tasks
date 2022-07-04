def duplicates_count(text):
    symbols = {symbol for symbol in text.lower() if text.lower().count(symbol) > 1}
    return len(symbols)


if __name__ == '__main__':
    users_text = input('Enter your text to know quantity of duplicates: ')
    print(f'Quantity of duplicates in your text: {duplicates_count(users_text)}')
