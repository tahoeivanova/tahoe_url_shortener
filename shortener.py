'''
ADDITTIONAL OPTION OF URL-SHORTENER
URL-Shortener DICT
'''

class UrlShortener:
    # short_url = id (id уникальны)
    url_dict = {} # ключи - original_url, значение - id
    id = 1

    def shorten_url(self, original_url):
        if original_url in self.url_dict:
            id = self.url_dict[original_url]
            shorten_url = self.base_62_encoder(id)
        else:
            self.url_dict[original_url] = self.id
            shorten_url = self.base_62_encoder(self.id)
            self.id += 1

        return f'localhost/{str(shorten_url)}'


    def base_62_encoder(self, id):
        charecters = '0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        base = len(charecters)
        result = []
        while id > 0:
            val = id % base
            result.append(charecters[val])
            id = id//base
        return ''.join(result[::-1])

if __name__ == '__main__':
    url_1 = 'https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/'
    url_2 = 'https://ru.wikibooks.org/wiki/Flask'
    url_3 = 'https://github.com/tahoeivanova/hh_api_requirements/blob/master/my_flask.py'

    shortener = UrlShortener()
    print(shortener.shorten_url(url_1))
    print(shortener.shorten_url(url_2))
    print(shortener.shorten_url(url_3))

