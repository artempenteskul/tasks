# codility digrams problem

def solution(s):
    results = []
    init_digrams = {}
    for letter_index, letter in enumerate(s):
        if letter_index + 1 < len(s):
            current_digram = f'{letter}{s[letter_index+1]}'
            if current_digram in init_digrams:
                results.append(letter_index - init_digrams[current_digram])
            else:
                init_digrams[current_digram] = letter_index

    return max(results) if results else -1


if __name__ == '__main__':
    print(solution('aakmaakmakda'))  # 7
    print(solution('aaa'))  # 1
    print(solution('codility'))  # -1
