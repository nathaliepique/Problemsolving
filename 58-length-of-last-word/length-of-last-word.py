class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        count = 0

        while i >= 0:
            if s[i] == ' ' and count == 0:
                i -= 1
                continue
            if s[i] != ' ':
                count += 1
            else:
                break
            i -= 1
        return count
