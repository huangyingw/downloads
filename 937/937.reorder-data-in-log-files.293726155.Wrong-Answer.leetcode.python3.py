class Solution:
    def reorderLogFiles(self, logs):
        digit_logs = []
        letter_logs = []
        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda a: a.split()[1:])
        return letter_logs + digit_logs

