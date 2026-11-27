class Solution:
    def shortestPathBinaryMatrix(self,grid):
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q=[(0,0,1)]
        grid[0][0]=1
        while q:
            r,c,steps=q.pop(0)
            if r==n-1 and c==n-1:
                return steps
            for i in range(-1,2):
                for j in range(-1,2):
                    nr=r+i
                    nc=c+j
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        q.append((nr,nc,steps+1))
        return -1