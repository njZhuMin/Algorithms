# Given a list of numbers that may has duplicate numbers, return all possible subsets
# NOTE: Each element in a subset must be in non-descending order.
#       The ordering between two subsets is free.
#       The solution set must not contain duplicate subsets.
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    # Recursive_DFS
    # Notice: dfs(num, i + 1, list, ret);中的 i + 1 不可误写为 pos + 1
    # pos用于每次大的循环，i用于内循环
    # 时间复杂度近似O(2^n)
    def subsetsWithDup(self, nums):
        if nums is None:
            return []
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, pos, list_temp, ret):
        # append new object with []
        ret.append([] + list_temp)
        for i in range(pos, len(nums)):
            if i != pos and nums[i] == nums[i - 1]:
                continue
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 2]
    print(s.subsetsWithDup(arr))



