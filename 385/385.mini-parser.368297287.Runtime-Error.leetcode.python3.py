"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Note: You may assume that the string is well-formed:
String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:
Given s = "324",
You should return a NestedInteger object which contains a single integer 324.
Example 2:
Given s = "[123,[456,[789]]]",
Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
"""


class NestedInteger:
    def __init__(self, value=None):

    def isInteger(self):

    def add(self, elem):

    def setInteger(self, value):

    def getInteger(self):

    def getList(self):


class Solution:
    def deserialize(self, s):

        return eval(s)


class Solution:
    def deserialize(self, s):

        if s[0] != '[':
            return NestedInteger(int(s))
        res = NestedInteger()
        stack = [res]
        i, j = 1, 1
        while stack:
            if s[j] == '-':
                j += 1
            while s[j].isdigit():
                j += 1
            if i != j:
                stack[-1].add(int(s[i:j]))
            if s[j] == ']':
                r = stack.pop()
                if stack:
                    stack[-1].add(r)
            elif s[j] == '[':
                stack.append(NestedInteger())
            j += 1
            i = j
        return res

