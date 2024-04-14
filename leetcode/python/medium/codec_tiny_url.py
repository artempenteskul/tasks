# task number - 535

from uuid import uuid4


class Codec:
    def __init__(self):
        self.db = dict()

    def encode(self, long_url: str) -> str:
        hash_url = str(uuid4())
        self.db[hash_url] = long_url
        return hash_url

    def decode(self, short_url: str) -> str:
        if short_url not in self.db:
            raise ValueError('Invalid short_url passed.')

        return self.db[short_url]


if __name__ == '__main__':
    codec = Codec()
    test = codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl'))
    print(f'Test result - {test}')
