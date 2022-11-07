def to_camel_case(text: str):
    words = text.replace('-', '_').split('_')
    if words[0] == words[0].capitalize():
        words[0].capitalize()
    res = [x.capitalize() for x in words[1:]]
    return words[0] + ''.join(res)


if __name__ == '__main__':
    print(to_camel_case('the_stealth_warrior'))
    print(to_camel_case('The-Stealth-Warrior'))
