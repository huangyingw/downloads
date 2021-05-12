class TwoSum(object):

    def __init__(self):
        self.number_to_count = {}

    def add(self, number):
        self.number_to_count[number] = self.number_to_count.get(number, 0) + 1
        print("number_to_count --> %s" % str(self.number_to_count))

    def find(self, value):
        print("value --> %s" % value)
        for num, count in enumerate(self.number_to_count):
            print("num --> %s" % num)
            y = value - num

            if y == num:
                if count >= 2:
                    print("count --> %s" % count)
                    return True
            elif y in self.number_to_count:
                print("y --> %s" % y)
                return True

        return False

