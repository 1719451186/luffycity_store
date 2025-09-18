from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x-1, y), # 上
    lambda x,y: (x, y+1), # 右
    lambda x,y: (x+1, y), # 下
    lambda x,y: (x, y-1)  # 左
]

def print_r(path):
    real_path = []
    i = len(path) - 1
    while i >= 0:
        real_path.append(path[i][0:2])
        i = path[i][2]
    real_path.reverse()
    for p in real_path:
        print(p)

def maze_path_queue(x1, y1, x2, y2): # x1, y1为起点坐标，x2, y2为终点坐标
    queue = deque()
    path = []
    queue.append((x1, y1, -1)) # 起点入队，-1表示没有前驱节点
    # 如果队列空了，说明，这个起点是没有路的
    while (len(queue) > 0):
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 到达重点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2 # 走过的路标记为2
    return False

maze_path_queue(1, 1, 7, 13)