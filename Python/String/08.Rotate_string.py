# Given a string and an offset, rotate string by offset.
# rotate s[0:offset]
# rotate s[offset:len(s)]
# rotate whole s
class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        if s is None or len(s) == 0:
            return s
        offset %= len(s)
        before = s[:len(s) - offset]
        after = s[len(s) - offset:]
        # [::-1] means reverse in Python
        s = before[::-1] + after[::-1]
        s = s[::-1]
        return s

if __name__ == '__main__':
    s = Solution()
    array = "abcdefg"
    print(s.rotateString(array, 3))