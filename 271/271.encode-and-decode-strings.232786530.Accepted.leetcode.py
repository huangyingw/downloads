class Codec:
    def encode(self, strs):
        return ''.join(s.replace('|', '||') + ' | ' for s in strs)

    def decode(self, s):
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]

