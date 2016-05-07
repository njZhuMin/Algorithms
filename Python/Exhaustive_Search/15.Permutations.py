# Given a list of numbers, return all possible permutations.
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # Recursion_Definition
    # 要求给定数组的全排列，模拟为某个袋子里有编号为1到n的球，将其放入n个不同的盒子
    # 基本思路就是从袋子里逐个拿球放入盒子，直到袋子里的球拿完为止，拿完时即为一种放法
    # 复杂度：  由于取的结果都是最终结果，无需去重判断，时间复杂度为 O(n!)
    #       但是由于nums[:i] + nums[i + 1:] 会产生新的列表，实际运行比Recursion_(Subsets template)慢不少
    def permute(self, nums):
        # 使用len()时需防止None
        # 递归终止条件为数组中仅剩一个元素或为空，否则遍历nums数组，取出第i个元素并将其加入至最终结果
        # nums[:i] + nums[i+1:]即为去掉第i个元素后的新列表
        if nums is None:
            return []
        elif len(nums) <= 1:
            return [nums]

        result = []
        for i, item in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                result.append(p + [item])
        return result


class Solution2:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # Recursion (Subsets template)
    # 复杂度:  以状态数来分析，最终全排列个数应为n!
    #       每个节点被遍历的次数为(n − 1)!，节点共被遍历的状态数为	O(n!)
    #       若不对list中是否包含nums[i]进行检查,则总的状态数应为 n^n 种
    #       由于最终的排列结果中每个列表的长度都为n，各列表的相同元素并不共享，故时间复杂度的下界为O(n×n!)
    #       上界为 n×n^n. 实测helper中for循环的遍历次数在 O(2n×n!)	以下
    def permute(self, nums):
        # 取结果时只取 list.size() == nums.size()	的解
        # 添加list元素的时候需要注意除重以满足全排列的要求
        # 假设前提为输入数据中无重复元素
        alist = []
        result = []
        if not nums:
            return result
        self.backTrack(nums, alist, result)
        return result

    def backTrack(self, nums, alist, ret):
        if len(alist) == len(nums):
            # Create new object every time list.append() is called
            ret.append([] + alist)
            return

        for i, item in enumerate(nums):
            if item not in alist:
                alist.append(item)
                self.helper(nums, alist, ret)
                alist.pop()


class Solution3:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    # 基于C++ STL中next_permutation的字典序实现方法
    # 1. 从后往前寻找索引满足 a[k] < a[k + 1]，如果此条件不满足，则说明已遍历到最后一个
    # 2. 从后往前遍历，找到第一个比 a[k] 大的数 a[l]，即 a[k] < a[l]
    # 3. 交换 a[k] 与  a[l]
    # 4. 反转 k + 1 ~ n 之间的元素
    def permute(self, nums):
        if nums is None:
            return []
        elif len(nums) <= 1:
            return [nums]

        # sort nums first
        nums.sort()
        result = []
        while True:
            result.append([] + nums)
            # step1: find nums[i] < nums[i + 1], Loop backwards
            i = 0
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
                elif i == 0:
                    return result
            # step2: find nums[i] < nums[j], Loop backwards
            j = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    break
            # step3: swap between nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # step4: reverse between [i + 1, n - 1]
            nums[i + 1:len(nums)] = nums[len(nums) - 1:i:-1]
        return result


if __name__ == '__main__':
    s = Solution3()
    nums = [1, 2, 3]
    print(s.permute(nums))