class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rot_oranges = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rot_oranges.append((r, c))
        
        if fresh_count == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        min = 0
        
        while rot_oranges and fresh_count > 0:
            min += 1
            for _ in range(len(rot_oranges)):
                r, c = rot_oranges.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        rot_oranges.append((nr, nc))
            
        return min if fresh_count == 0 else -1
        
        