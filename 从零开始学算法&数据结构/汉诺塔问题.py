# n 是 n 个盘子，a 是起始柱子，b 是辅助柱子，c 是目标柱子
def hanoi(n, a, b, c ): 
    if n>0:
        hanoi(n-1, a, c, b) # 先把 n-1 个盘子从 a 借助 c 移动到 b
        print(a, '-->', c) 
        hanoi(n-1, b, a, c) # 再把 n-1 个盘子从 b 借助 a 移动到 c


