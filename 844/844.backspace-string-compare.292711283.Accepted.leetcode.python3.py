class Solution(object):
    def backspaceCompare(self, S, T):
        s_i, t_i = len(S) - 1, len(T) - 1

        def next_char(string, i):
            delete = 0
            while i >= 0 and (delete or string[i] == "#"):
                delete = delete + 1 if string[i] == "#" else delete - 1
                i -= 1
            return i
        while True:
            s_i = next_char(S, s_i)
            t_i = next_char(T, t_i)
            if s_i == -1 and t_i == -1:
                return True
            if s_i == -1 or t_i == -1:
                return False
            if S[s_i] != T[t_i]:
                return False
            s_i -= 1
            t_i -= 1

