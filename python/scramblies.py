def scramble(s1: str, s2: str):
    for letter in s2:
        if letter not in s1 or s1.count(letter) < s2.count(letter):
            return False
    return True


if __name__ == '__main__':
    print(scramble('rkqodlw', 'world'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
