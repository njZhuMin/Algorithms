class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    # 只需要统计出现次数，典型的需要借助 Hash表 实现的题
    # 题中字符串中的字符可以假定为 ascii 码，使用256个 ascii 码处理
    # 1. 如何知道给定字符串中某一窗口长度已包含目标字符串中的全部字符(可能重复)?
    #   遍历给定字符串，如果给定字符串中出现的字符次数小于目标字符串，更新总的字符出现次数
    # 2. 在包含目标字符串中全部字符后，再出现目标字符串中的其他字符串时如何处理?
    #   通过维护窗口起止索引(两根指针)，在给定字符串中出现目标字符串中的全部字符时
    #   向前移动窗口起始处，若窗口长度小于之前的窗口长度，则更新最终答案要求的窗口起始索引
    def minWindow(self, source, target):
        if source is None or target is None:
            return ""
        if len(source) < len(target):
            return ""
        # ASCII码占 7 位，用 8 bit表示，最高位恒为0
        ASCII_COUNT = 256
        INT_MAX = 65535
        targetCount = [0] * ASCII_COUNT
        sourceCount = [0] * ASCII_COUNT
        for i in range(len(target)):
            ch2i = ord(target[i])
            targetCount[ch2i] += 1

        # target string character appeared in source string
        winStart = 0
        winMinStart = 0
        winMin = INT_MAX
        occurence = 0
        for winEnd in range(len(source)):
            # convert character to integer
            ch2i = ord(source[winEnd])
            sourceCount[ch2i] += 1
            # character occur in both source and target
            if targetCount[ch2i] > 0 and targetCount[ch2i] >= sourceCount[ch2i]:
                occurence += 1
            # adjust window size if all the target char occur in source
            if occurence == len(target):
                ch2i2 = ord(source[winStart])
                while sourceCount[ch2i2] > targetCount[ch2i2]:
                    sourceCount[ch2i2] -= 1
                    winStart += 1
                    ch2i2 = ord(source[winStart])
                # update winMinStart
                if winMin > winEnd - winStart + 1:
                    winMin = winEnd - winStart + 1
                    winMinStart = winStart

        if winMin == INT_MAX:
            return ""
        else:
            return source[winMinStart : winMinStart + winMin]

if __name__ == '__main__':
    s = Solution()
    # source = "ADOBECODEBANC"
    # target = "ABC"
    source = ""
    target = ""
    print(s.minWindow(source, target))
