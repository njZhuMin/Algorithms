class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
        # @param {integer[]} nums
        # @return {integer[][]}
    def permute(self, nums):
        if nums is None:
            return []
        elif len(nums) <= 1:
            return [nums]
        result = []
        for i, item in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                result.append(p + [item])
        return result
