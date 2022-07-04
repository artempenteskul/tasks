def is_isogram(string):
    if len(string) == 0:
        return True
    for letter in string:
        if string.lower().count(letter) > 1:
            return False
    return True


if __name__ == '__main__':
    print(is_isogram('Dermatoglyphics'))
    print(is_isogram('abA'))
    print(is_isogram('isogram'))
