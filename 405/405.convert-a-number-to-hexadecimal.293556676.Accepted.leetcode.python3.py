class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        mod_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

        def hexHelper(num, digits):
            return digits if num == 0 else hexHelper(num // 16, str(mod_map.get(int(num % 16)) or num % 16) + digits)
        return hexHelper(num, "")

