# For a given sorted array (ascending order) and a target number,
# find the first index of this number in O(log n) time complexity.
# if the target number does not exist in the array, return -1.
# Challenge: If the count of numbers is bigger than 2^32, can your code work properly?
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1

        start, end = -1, len(nums)
        while start + 1 < end:
            # avoid overflow when (end + start)
            mid = start + (end - start) // 2
            # use lower_bound
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if end == len(nums) or nums[end] != target:
            return -1
        else:
            return end

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 3, 4, 5, 10]
    print(s.binarySearch(nums, 4))