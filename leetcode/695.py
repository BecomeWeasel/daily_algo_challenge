from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dy=[1,-1,0,0]
        dx=[0,0,-1,1]
        max_area=0
        w,h=len(grid[0]),len(grid)
        
        visit=[[False for _ in range(w)] for _ in range(h)]
        
        # BFS T:O(w*h) S:O(w*h) 
        def island_bfs(sy,sx)->int:
            q=deque()
            q.append((sy,sx))
            area=1
            
            while q:
                y,x=q.popleft()
                for k in range(4):
                    ny,nx=y+dy[k],x+dx[k]

                    if not (0<=ny<h and 0<=nx<w):
                        continue
                            
                    if not visit[ny][nx] and grid[ny][nx]==1:
                        visit[ny][nx]=True
                        area+=1
                        q.append((ny,nx))
                        
            return area
        
        # DFS T:O(w*h) S:O(1) 
        def island_dfs(y,x)->int:
            # 벗어나거나 물이면
            if not (0<=y<h and 0<=x<w) or grid[y][x]==0:
                return 0
            else:
                # 땅을 방문하면서 0으로 바꿔서 visit 없이도 중복탐색 방지
                grid[y][x]=0
                
                u=island_dfs(y-1,x)
                d=island_dfs(y+1,x)
                l=island_dfs(y,x-1)
                r=island_dfs(y,x+1)
                
                return u+d+l+r+1
        
        for i in range(h):
            for j in range(w):
                if grid[i][j]==1:
                    ''' BFS
                    # visit[i][j]=True
                    # max_area=max(island_bfs(i,j),max_area)
                    '''
                    max_area=max(island_dfs(i,j),max_area)
                    
        
        return max_area
                              
        
                                     
