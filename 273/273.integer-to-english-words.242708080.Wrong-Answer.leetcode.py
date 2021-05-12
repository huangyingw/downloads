class Solution(object):
    def numberToWords(self, num):
        result = self.convertHundred(num % 1000)
        v = ["Thousand", "Million", "Billion"]
        result = result.strip()
        return result if result else "Zero"

    def convertHundred(self, num):
        v1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
              "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                       "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
              ]
        v2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
              "Seventy", "Eighty", "Ninety"
              ]
        result = ''
        a, b, c = num / 100, num % 100, num % 10
        result = v1[b] if b < 20 else v2[b / 10] + (" " + v1[c] if c > 0 else "")
        if a > 0:
            result = v1[a] + " Hundred" + (" " + result if b > 0 else "")
        return result

