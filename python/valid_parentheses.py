rp = '('
lp = ')'


def valid_parentheses(s):
    count = 0
    for i in s:
        if i == rp:
            count += 1
        if i == lp:
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False


if __name__ == '__main__':
    print(f'Is text valid: {valid_parentheses(s="hi())(")}')  # should return false
    print(f'Is text valid: {valid_parentheses(s="hi(hi)()")}')  # should return true
