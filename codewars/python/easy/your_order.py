def order(sentence: str):
    words = sentence.split()
    res = ''
    for i in range(1, 10):
        for word in words:
            if str(i) in word:
                res += f'{word} '
    return res


if __name__ == '__main__':
    print(order('4of Fo1r pe6ople g3ood th5e the2'))
    print(order('is2 Thi1s T4est 3a'))
