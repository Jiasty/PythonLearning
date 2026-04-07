# 求和函数
def SumFunc1(begin, end):
    total = 0
    for i in range(begin, end + 1):
        total += i
    print(total)


# 更推荐，解耦
def SumFunc2(begin, end):
    total = 0
    for i in range(begin, end + 1):
        total += i
    return total


SumFunc1(1, 100)
ret = SumFunc2(1, 100)
print(ret)

# 判定是否是奇数
def isOdd(num):
    if num % 2 == 0:
        return False
    return True


result = isOdd(10)
print(result)

# 返回多个值, 多元赋值
def getPoint():
    x = 10
    y = 20
    z = 30
    return x, y, z


# 不关心第三个返回值
a, b, _ = getPoint()
print(a)
print(b)
