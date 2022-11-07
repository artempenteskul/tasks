def find_missing_letter(chars):
    ords = [ord(x) for x in chars]
    prev = ords[0]
    res = None
    for i in ords[1:]:
        if i != prev + 1:
            res = prev + 1
            break
        prev = i
    return chr(res)


if __name__ == '__main__':
    print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
    print(find_missing_letter(['O', 'Q', 'R', 'S']))
