def alphanumeric(password):
    if len(password) == 0:
        return False
    if all(not letter.isspace() and 'a' <= letter.lower() <= 'z' or '0' <= letter <= '9' for letter in password):
        return True
    return False


if __name__ == '__main__':
    print(alphanumeric(password='    '))
    print(alphanumeric('PassW0rd'))
    print(alphanumeric('&)))((('))
