def likes(names: list):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


if __name__ == '__main__':
    users_names = []
    name = input('Enter the name of the person, who likes it or press ENTER to submit: ')
    while name != '':
        users_names.append(name)
        name = input('Enter the name of the next person or press ENTER to submit: ')
