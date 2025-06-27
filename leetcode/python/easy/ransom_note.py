# task number - 383
# topics - hash table, counting, string


from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_note_counter = Counter(ransom_note)
    magazine_counter = Counter(magazine)

    for letter in ransom_note_counter:
        if ransom_note_counter[letter] > magazine_counter[letter]:
            return False

    return True


if __name__ == '__main__':
    input_ransom_note = 'a'
    input_magazine = 'b'
    print(f'Can construct ransom note from magazine - {can_construct(input_ransom_note, input_magazine)}')  # false

    input_ransom_note = 'aa'
    input_magazine = 'ab'
    print(f'Can construct ransom note from magazine - {can_construct(input_ransom_note, input_magazine)}')  # false

    input_ransom_note = 'aa'
    input_magazine = 'aab'
    print(f'Can construct ransom note from magazine - {can_construct(input_ransom_note, input_magazine)}')  # true
