import time
# 计算函数运行时间的装饰器
def cal_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 运行时间: {end - start:.6f} 秒")
        return result
    return wrapper