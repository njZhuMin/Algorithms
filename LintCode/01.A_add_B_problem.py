# 不用加减法实现加法，类似数字电路中的全加器
# 异或求得部分和，相与求得进位，最后将进位作为加法器的输入，典型的递归实现思路
# 对于Python，int不会位溢出，需手动给出溢出标志
MAX_BIT = 2**32
MAX_BIT_COMPLIMENT = -2**32

class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        while b != 0:
            if b == MAX_BIT:
                return a ^ MAX_BIT_COMPLIMENT
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

if __name__ == '__main__':
    s = Solution()
    print(s.aplusb(8, -10))