class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0=1
        for i in range(len(matrix)):
            if(matrix[i][0]==0):
                col0=0
            for j in range(1,len(matrix[i])):
                if(matrix[i][j]==0):
                    matrix[0][j]=0
                    matrix[i][0]=0
        print(matrix)
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,0,-1):
                if(matrix[0][j]==0 or matrix[i][0]==0):
                    matrix[i][j]=0
            if(col0==0):
                matrix[i][0]=0