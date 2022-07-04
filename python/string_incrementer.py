def increment_str(text: str):
    stripped = text.rstrip('0123456789')
    nums = text[len(stripped):]

    if len(nums) == 0:
        return text + '1'

    res = int(nums) + 1
    res = str(res).zfill(len(nums))
    return stripped + res


if __name__ == '__main__':
    print(increment_str('hello'))
    print(increment_str('hello02'))
    print(increment_str('foobar99'))
