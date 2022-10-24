def scramble(s1, s2):
    if all(letter in s1 for letter in s2):
        return True
    return False


if __name__ == '__main__':
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
