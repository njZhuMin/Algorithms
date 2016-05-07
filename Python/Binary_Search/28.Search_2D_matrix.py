class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        # first pos >= target
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][-1] <= target:
                start = mid
            else:
                end = mid
        if matrix[start][-1] >= target:
            row = matrix[start]
        elif matrix[end][-1] >= target:
            row = matrix[end]
        else:
            return False

        # binary search in row
        start, end = 0, len(row) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid
            else:
                end = mid
        return row[start] == target or row[end] == target

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20],[23, 30, 34, 50]]
    print(s.search_matrix(matrix, 3))