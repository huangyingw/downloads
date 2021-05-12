class Codec:
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        self.count = 0

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            self.count += 1
            self.code2url[str(self.count)] = longUrl
            self.url2code[longUrl] = str(self.count)
        return "http:/tinyurl.com/" + str(self.count)

    def decode(self, shortUrl):
        return self.code2url[shortUrl.split('/')[-1]]

