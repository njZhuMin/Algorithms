# Merge two given sorted integer array A and B into a new sorted integer array.
class Solution:
    # @param A and B: sorted integer array A and B.
    # @return: A new sorted integer array
    def	mergeSortedArray(self, A, B):
        if A is None or len(A) == 0:
            return B
        if B is None or len(B) == 0:
            return A
        C = []
        aLen, bLen = len(A), len(B)
        i, j = 0, 0
        while i < aLen and j < bLen:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1

        # A has elements left
        while i < aLen:
            C.append(A[i])
            i += 1

        # B has elements left
        while j < bLen:
            C.append(B[j])
            j += 1

        return C

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = [2, 4, 5, 6]
    s = Solution()
    print(s.mergeSortedArray(A, B))