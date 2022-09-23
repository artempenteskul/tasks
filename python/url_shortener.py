import string
import random


SHORT_URLS = {}
LONG_URLS = {}


class UrlShortener:

    def shorten(self, long_url):
        if long_url in LONG_URLS:
            return LONG_URLS[long_url]

        short_url = self._get_short_url()
        while short_url in SHORT_URLS:
            short_url = self._get_short_url()

        SHORT_URLS[short_url] = long_url
        LONG_URLS[long_url] = short_url

        return short_url

    @staticmethod
    def _get_short_url():
        base_url = 'short.ly/'
        url_id = ''.join(random.choices(string.ascii_letters.lower(), k=8))
        short_url = f'{base_url}{url_id}'
        return short_url

    def redirect(self, short_url):
        return SHORT_URLS[short_url]


if __name__ == '__main__':
    url_shortener = UrlShortener()
    short_url1 = url_shortener.shorten('https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f')
    short_url2 = url_shortener.shorten('https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f')
    short_url3 = url_shortener.shorten('https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f11')
    print(short_url1)
    print(short_url2)
    print(short_url3)
