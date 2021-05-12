class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.dic = {}  # 空字典
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            # 如果词长度小于等于2，就是这个词本身存入字典，否则遵循abbreviation规则
            self.dic[abb] = word if abb not in self.dic else "" if self.dic[abb] != word else self.dic[abb]
            # 1. 如果abbreviation之后的词不在字典中，直接存入
            # 2. 如果童谣的abbreviation结果已经存在了，但是value的词不是同一个，即abbreviation之后对应多个词，那么直接把value存为""。因为这样的abbreviation不符合no other word这个条件，肯定会返回False。
            # 3. abbreviation对应的已经在字典中的本身value

    def isUnique(self, word):
        abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abb not in self.dic or self.dic[abb] == word
        # 因为abbreviation对应多个词的可能性我们已经给了""的value，所以可以直接判断
        # 1. 不在字典中
        # 2. 在字典中，且刚好是同一个词

