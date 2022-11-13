class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        return self.vigenere_cipher(text, 'encode')

    def decode(self, text):
        return self.vigenere_cipher(text, 'decode')

    def vigenere_cipher(self, text, mode):
        res_text = ''
        key_index = 0
        for char in text:
            if char not in self.alphabet:
                res_text += char
            else:
                char_index = self.alphabet.index(char)
                char_index_offset = self.alphabet.index(self.key[key_index])

                if mode == 'encode':
                    res_char_index = (char_index + char_index_offset) % len(self.alphabet)
                elif mode == 'decode':
                    res_char_index = (char_index - char_index_offset)
                    if res_char_index < 0:
                        res_char_index = len(self.alphabet) - abs(res_char_index)
                else:
                    raise Exception('Unsupported mode for the method!')

                res_text += self.alphabet[res_char_index]

                if key_index == len(self.key) - 1:
                    key_index = 0
                else:
                    key_index += 1

        return res_text


if __name__ == '__main__':
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)

    print(c.encode('codewars'))
    print(c.decode('rovwsoiv'))
    print()

    print(c.encode('waffles'))
    print(c.decode('laxxhsj'))
    print()

    print(c.encode('CODEWARS'))
    print(c.decode('CODEWARS'))
