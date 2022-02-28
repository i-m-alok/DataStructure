class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)-1
        n=len(matrix[0])-1
        #invert matrix
        for i in range((m+1)//2):
            for j in range(n+1):
                matrix[i][j], matrix[m-i][j] = matrix[m-i][j], matrix[i][j]
        #start swaping nums[i][j] with nums[j][i]
        for i in range(m):
            for j in range(i+1,n+1):
                print(i,j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]     