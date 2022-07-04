def hashtag_generator(s: str):
    words = s.split()
    if len(words) < 1:
        return False
    res = '#'
    for word in words:
        res += word.title()
    return False if len(res) > 140 else res


if __name__ == '__main__':
    users_text = input('Enter tour text in order to make a hashtag: ')
    print(f'Your hashtag: {hashtag_generator(s=users_text)}')
