from collections import deque

def can_move(pos, graph):
    next_pos = []
    pos = list(pos)
    lx, ly, rx, ry = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nlx, nly, nrx, nry = lx+dx[i], ly+dy[i], rx+dx[i], ry+dy[i]
        if graph[nlx][nly] == 0 and graph[nrx][nry] == 0:
            next_pos.append({(nlx, nly), (nrx, nry)})
    if lx == rx: # 가로인 경우
        for i in [-1, 1]:
            if graph[lx+i][ly] == 0 and graph[rx+i][ry] == 0:
                next_pos.append({(lx,ly), (lx+i, ly)})
                next_pos.append({(rx, ry), (rx+i, ry)})
    elif ly == ry: # 세로인 경우
        for i in [-1, 1]:
            if graph[lx][ly+i] == 0 and graph[rx][ry+i] == 0:
                next_pos.append({(lx, ly), (lx, ly+i)})
                next_pos.append({(rx, ry), (rx, ry+i)})
    return next_pos

def solution(board):
    n = len(board) + 2
    m = len(board)
    graph = [[1]*n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            graph[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (m, m) in pos:
            return cost
        for next_pos in can_move(pos, graph):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)
    return 0
