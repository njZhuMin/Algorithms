# Given a set of distinct integers, return all possible subsets.
# NOTE: Elements in a subset must be in non-descending order.
#       The solution set must not contain duplicate subsets.
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    # Iterative_BitMap
    # 利用类似bitmap的原理，将c0~2n-1个数值map到每个index上
    # 如输入[1 ,2 ,3]，000 -> [] ; 001 -> [1] ; ... ; i = 7, 111 -> [1, 2, 3]
    def subsets(self, S):
        if not S:
            return []
        ret = []
        S.sort()
        n = len(S)
        for i in range(2**n):
            tmp = []
            for j in range(n):
                if i & (1 << j):
                    tmp.append(S[j])
            ret.append(tmp)
        return ret


class Solution2:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    # Recursive_DFS
    # Notice: dfs(num, i + 1, list, ret);中的 i + 1 不可误写为 pos + 1
    # pos用于每次大的循环，i用于内循环
    # 时间复杂度近似O(2^n)
    def subsets(self, nums):
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
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()

if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3]
    print(s.subsets(arr))



