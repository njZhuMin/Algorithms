class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []
        count = 0
        self.resultList = []
        row = []
        self.used = [False for i in range(n)]
        self.nQueenHelper(row, n)
        result = self.getMatrix(self.resultList, n)
        return result

    def getMatrix(self, resultList, n):
        result = []
        for i in range(len(resultList)):
            string = ""
            for j in range(n):
                string += "."
            matrix = [string for j in range(n)]
            for k in range(len(resultList[i])):
                st = matrix[k]
                st = list(st)
                index = resultList[i][k]
                st[index] = "Q"
                matrix[k] = "".join(st)
            result.append(matrix)
        return result

    def nQueenHelper(self, row, n):
        if len(row) == n:
            newList = list(row)
            self.resultList.append(newList)
        for j in range(n):
            if not self.used[j]:
                row.append(j)
                if self.checkValid(row):
                    self.used[j] = True
                    self.nQueenHelper(row, n)
                    row.pop()
                    self.used[j] = False
                else:
                    row.pop()

    def checkValid(self, row):
        length = len(row)
        for i in range(length):
            for j in range(i+1, length):
                if abs(row[j] - row[i]) == abs(j-i):
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(1))