class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        temp = [1]
        for i in range(1,numRows):
            for j in range(1,i):
                temp[j]=result[i-1][j]+result[i-1][j-1]
            temp.append(1)
            result.append(deepcopy(temp))
        return result