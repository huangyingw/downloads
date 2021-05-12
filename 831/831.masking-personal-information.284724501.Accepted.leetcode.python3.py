class Solution(object):
    def maskPII(self, S):
        if "@" in S:
            name, address = S.lower().split("@")
            return name[0] + "*****" + name[-1] + "@" + address
        digits = [c for c in S if "0" <= c <= "9"]
        country, local = digits[:-10], digits[-10:]
        result = []
        if country:
            result = ["+"] + ["*"] * len(country) + ["-"]
        result += ["***-***-"] + local[-4:]
        return "".join(result)

