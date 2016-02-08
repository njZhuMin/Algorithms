# For a given source string and a target string,
# you should output the first index(from 0) of target string in source string.
# If target does not exist in source, just return -1.
# apply KMP Algorithm to make it in cost O(n)
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:  # no break
                return i
        return -1
