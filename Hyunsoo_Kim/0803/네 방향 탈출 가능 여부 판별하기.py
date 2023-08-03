from collections import deque

n, m = map(int, input().split())

gh = []
visited = [[False for _ in range(m)] for _ in range(n)]


for i in range(n):
    gh.append(list(map(int, input().split())))

q = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            if visited[nx][ny]:
                continue
            if gh[nx][ny]==0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True

q.append((0,0))
visited[0][0] = True

bfs()

if visited[n-1][m-1]:
    print("1")
else:
    print("0")
