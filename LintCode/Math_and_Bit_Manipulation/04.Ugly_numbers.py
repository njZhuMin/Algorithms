# 丑陋数的因子也必定是丑陋数，它一定是某个丑陋数乘3,5,7得到的
# 问题在于，小的丑陋数乘5不一定比大的丑陋数乘2要小
# 我们没法直接使用目前最大的丑陋数来乘3,5,7顺序得到更大的丑陋数
# 不过，可以确定的是，小的丑陋数乘2，肯定小于大的丑陋数乘2
# 维护三个指针分别记录乘3,5,7得出的目前最大丑陋数，通过比较当前最大丑陋数与生成最小丑陋数，生成下一个丑陋数
# 复杂度 O(n) in time, O(n) in mem
class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        arr = []
        arr.append(1)
        index3 = 0
        index5 = 0
        index7 = 0
        if k < 0:
            return -1
        while len(arr) < k+1:
            num3 = arr[index3] * 3
            num5 = arr[index5] * 5
            num7 = arr[index7] * 7
            nextnum = min(num3, num5, num7)
            arr.append(nextnum)
            if nextnum == num3: index3 += 1
            if nextnum == num5: index5 += 1
            if nextnum == num7: index7 += 1
        return arr[k]

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 10):
        print(s.kthPrimeNumber(i))

