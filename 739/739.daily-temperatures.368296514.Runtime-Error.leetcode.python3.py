"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
"""


class Codec:
    def encode(self, longUrl):

        self.hash = {}
        if longUrl not in self.hash:
            idx = hash(longUrl)
            self.hash[idx] = longUrl
        final_string = 'https://tinyurl.com/' + str(idx)
        return (final_string)

    def decode(self, shortUrl):

        v = shortUrl[20:len(shortUrl)]
        return (self.hash[int(v)])

