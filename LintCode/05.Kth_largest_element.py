# Find K-th largest element in an array.
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        ans = self.select(A, 0, len(A)-1, k-1)
        return ans

    # @param num an integer array
    # @param left left bound
    # @param right right bound
    def partition(self, num, left, right):
        pivot = num[left]
        i = left
        j = right
        while i < j:
            while pivot < num[j] and i < j:
                j -= 1
            if i < j:
                num[i] = num[j]
                i += 1
            while pivot > num[i] and i < j:
                i += 1
            if i < j:
                num[j] = num[i]
                j -= 1
        num[i] = pivot
        return i

    # @param num an integer array
    # @param left left bound
    # @param right right bound
    # @param k the kth major element
    def select(self, num, left, right, k):
        if left == right:
            return num[left]
        i = self.partition(num, left, right)
        j = i - left
        if j == k:
            return num[i]   #分割完后，如果pivot刚刚好就是第K大，直接返回，否则还有两种情况：
        if j < k:
            return self.select(num, i+1, right, k-j-1)
        else:
            return self.select(num, left, i-1, k)

if __name__ == '__main__':
    s = Solution()
    A = [9, 3, 2, 4, 8]
    print(s.kthLargestElement(3, A))