class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1]]
        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            ans = []
            for j in range(len(temp)-1):
                ans.append(temp[j]+temp[j+1])
            res.append(ans)
        return res[-1]