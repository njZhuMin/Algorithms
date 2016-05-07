# Given a list of numbers with duplicate number in it. Find all unique permutations.
class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        alist = []
        result = []
        visited = [False] * len(nums)
        if not nums:
            return result

        # important! sort before call `backTrack`
        nums.sort()
        self.backTrack(nums, alist, visited, result)
        return result

    def backTrack(self, nums, alist, visited, ret):
        if len(alist) == len(nums):
            # Create new object every time list.append() is called
            ret.append([] + alist)
            return

        for i in range(len(nums)):
            if visited[i] or (i != 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            visited[i] = True
            alist.append(nums[i])
            self.backTrack(nums, alist, visited, ret)
            alist.pop()
            visited[i] = False


class Solution2:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    # 基于C++ STL中next_permutation的字典序实现方法
    # 1. 从后往前寻找索引满足 a[k] < a[k + 1]，如果此条件不满足，则说明已遍历到最后一个
    # 2. 从后往前遍历，找到第一个比 a[k] 大的数 a[l]，即 a[k] < a[l]
    # 3. 交换 a[k] 与  a[l]
    # 4. 反转 k + 1 ~ n 之间的元素
    def permuteUnique(self, nums):
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
    s = Solution2()
    nums = [1, 2, 2]
    print(s.permuteUnique(nums))