# Python对字符串的操作优于求余求模
# 转化为字符串处理
class Solution:
    # @param k & n  two integer
    # @return ans a integer
    def digitCounts(self, k, n):
        ans = 0
        for x in range(0, n+1):
            x = str(x)
            for digits in x:
                if int(digits) == k:
                    ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.digitCounts(1, 12))