# 打印1 - 10
num = 1
while num <= 10:
    print(num)
    num += 1

# 计算1 - 100的和
_sum = 0
pos = 1
while pos <= 100:
    _sum += pos
    pos += 1
print(_sum)

# 计算1! + 2! + 3! + 4! + 5!
_sum = 0
times = 1
while times <= 5:
    tmp = 1
    i = 1
    while i <= times:
        tmp *= i
        i += 1
    _sum += tmp
    times += 1
print(f'sum = {_sum}')