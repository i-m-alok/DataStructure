class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if(m==1 and n==1):
        #     return 1
        grid=[[0 for _ in range(n)] for _ in range(m)]
        count=0
        self.countUniquePaths(grid,0,0, count)
        return grid[0][0] 
    
    def countUniquePaths(self, grid, x,y, count):
        # print(x,y)
        if(x==len(grid)-1 and y==len(grid[0])-1):
            # count+=1
            grid[x][y]=1
            return 1
        
        #move right
        if(x<len(grid) and y+1<len(grid[0])):
            if(grid[x][y+1]>0):
                grid[x][y]+=grid[x][y+1]
            else:
                grid[x][y]+=self.countUniquePaths(grid, x, y+1, count)
            # print(x, y, grid)
        #move down
        if(x+1<len(grid) and y<len(grid[0])):
            if(grid[x+1][y]>0):
                grid[x][y]+=grid[x+1][y]
            else:
                grid[x][y]+=self.countUniquePaths(grid, x+1, y, count)
            # print(x, y, grid)
            
        return grid[x][y]