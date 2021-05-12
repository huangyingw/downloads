class TwoSum(object):

    def __init__(self):
        self.number_to_count = {}

    def add(self, number):
        self.number_to_count[number] = self.number_to_count.get(number, 0) + 1

    def find(self, value):

        for k, v in self.number_to_count.iteritems():
            y = value - k

            if y == k:
                if v >= 2:
                    return True
            elif y in self.number_to_count:
                return True

        return False

