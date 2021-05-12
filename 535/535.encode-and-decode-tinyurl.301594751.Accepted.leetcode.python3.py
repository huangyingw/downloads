class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(5))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return "http:/tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-5:]]

