class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]

        for _ in range(numRows-2):
            curr = [1]
            for i in range(len(ans[-1])-1):
                curr.append(ans[-1][i] + ans[-1][i+1])
            curr.append(1)
            ans.append(curr)
        return ans
    


########### Alternative Method
class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)

        return res   