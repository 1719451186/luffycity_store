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

def maze_path(x1, y1, x2, y2): # x1, y1为起点坐标，x2, y2为终点坐标
    stack = []
    stack.append((x1, y1)) # 起点入栈
    # 如果栈空了，说明，这个起点是没有路的
    while (len(stack) > 0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2: # 找到终点
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 走过的路标记为2
                break # 走过一条路就跳出for循环
        else: # 四个方向都走不通
            maze[nextNode[0]][nextNode[1]] = 2  # 走过的路标记为2
            stack.pop() # 回溯
    else:
        print("没有路")
        return False

maze_path(1, 1, 7, 13)