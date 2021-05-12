class TwoSum(object):

    def __init__(self):
        self.number_to_count = {}

    def add(self, number):
        self.number_to_count[number] = self.number_to_count.get(number, 0) + 1

    def find(self, value):
        for num, count in enumerate(self.number_to_count):
            y = value - num

            if y == num:
                if count >= 2:
                    return True
            elif self.number_to_count.containsKey(y):
                return True

        return False

