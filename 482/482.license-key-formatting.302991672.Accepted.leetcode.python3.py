class Solution(object):
    def licenseKeyFormatting(self, S, K):
        key = S.replace("-", "").upper()
        formatted = []
        i = len(key) - K
        while i >= 0:
            formatted.append(key[i:i + K])
            i -= K
        if i != -K:
            formatted.append(key[:i + K])
        return "-".join(formatted[::-1])
        return "-".join(formatted)

