#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (20.11%)
# Total Accepted:    163.1K
# Total Submissions: 810.9K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string!!!dict is a set type!!!
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        while queue:
            e, lens = queue.pop(0)
            if e == endWord:
                return lens
            for i in range(len(e)):
                left = e[:i]
                right = e[i + 1:]
                for c in 'abcdefghigklmnopqrstuvwxyz':
                    if e[i] != c:
                        nextWord = left + c + right
                        if nextWord in wordList:
                            queue.append((nextWord, lens + 1))
                            wordList.remove(nextWord)
        return 0

