class Codec:
    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        code = uuid.uuid4()
        self.code2url[str(code)] = longUrl
        return "http:/tinyurl.com/" + str(code)

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]

