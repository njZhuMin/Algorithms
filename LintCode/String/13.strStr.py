class Solution:
    def strStr(self, source, target):
        return self.KMPMatch(source, target)

    def KMPMatch(self, text, pattern):

        """
        Yields all starting positions of copies of the pattern in the text.
        Calling conventions are similar to string.find, but its arguments can be
        lists or iterators, not just strings, it returns all matches, not just
        the first one, and it does not need the whole text in memory at once.
        Whenever it yields, it will have read the text exactly up to and including
        the match that caused the yield.
        """
        if text is None or pattern is None:
            return -1
        if len(text) < len(pattern):
            return -1
        elif len(pattern) == 0:
            return 0
        
        # allow indexing into pattern and protect against change during yield
        pattern = list(pattern)

        # build table of shift amounts
        shifts = [1] * (len(pattern) + 1)
        shift = 1
        for pos in range(len(pattern)):
            while shift <= pos and pattern[pos] != pattern[pos-shift]:
                shift += shifts[pos-shift]
            shifts[pos+1] = shift

        # do the actual search
        startPos = 0
        matchLen = 0
        for c in text:
            while matchLen == len(pattern) or \
                    matchLen >= 0 and pattern[matchLen] != c:
                startPos += shifts[matchLen]
                matchLen -= shifts[matchLen]
            matchLen += 1
            if matchLen == len(pattern):
                return startPos
        return -1