# 找阶乘数中末尾的连零数量，即找相乘能为10的整数倍的数
# 即计算质因数5和2的个数中较小的一个，质因数2的个数显然要大于5的个数
# 故只需要计算给定阶乘数中质因数中5的个数
# 复杂度 O(log(n))
class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        if n < 0:
            ans = -1
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeros(11))