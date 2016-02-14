# Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # 在 (s1[i1] == s3[i3]) && (s2[i2] == s3[i3]) 时分两种情况考虑
        # 即让 s1[i1] 和 s3[i3] 配对或者 s2[i2] 和 s3[i3] 配对
        # 嵌套调用时新生成的字符串分别为 s1[1+i1:], s2[i2], s3[1+i3:] 和 s1[i1:], s2[1+i2], s3[1+i3:]
        # 嵌套调用结束后立即返回最终结果，不立即返回则有可能会产生错误结果
        # 递归调用并未影响到调用处的 i1 和 i2.
        len1 = 0 if s1 is None else len(s1)
        len2 = 0 if s2 is None else len(s2)
        len3 = 0 if s3 is None else len(s3)
        if len3 != len1 + len2:
            return False

        i1, i2 = 0, 0
        for i3 in range(len(s3)):
            result = False
            if (i1 < len1 and s1[i1] == s3[i3]) and (i1 < len1 and s1[i1] == s3[i3]):
                # s1[1+i1:], s2[i2:], s3[1+i3:]
                case1 = self.isInterleave(s1[1+i1:], s2[i2:], s3[1+i3:])
                # s1[i1:], s2[1+i2:], s3[1+i3:]
                case2 = self.isInterleave(s1[i1:], s2[1+i2:], s3[1+i3:])
                return case1 or case2
            if i1 < len1 and s1[i1] == s3[i3]:
                i1 += 1
                result = True
                continue
            if i2 < len2 and s2[i2] == s3[i3]:
                i2 += 1
                result = True
                continue
            # return instantly if both s1 and s2 can not pair with s3
            if not result:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s4 = "aadbbbaccc"
    print(s.isInterleave(s1, s2, s3))
    print(s.isInterleave(s1, s2, s4))
