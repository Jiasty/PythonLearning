# 求1-100的和
_sum = 0
for i in range(1, 101):
    _sum += i
print(_sum)


# 求100-1000的和
_sum = 0
for i in range(100, 1001):
    _sum += i
print(_sum)

# 定义求和函数
def theSumFunc(begin, end):
    total = 0
    for i in range(begin, end + 1):
        total += i
    return total


# 调用函数执行
ret = theSumFunc(1, 100)
print(ret)
