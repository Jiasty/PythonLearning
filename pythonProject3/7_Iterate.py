# 使用for循环遍历
a = [1, 2, 3]
for e in a:
    print(e)
    e += 10  # 不会改变原数组
print(a)


# 使用下标访问遍历
b = [1, 2, 3]
for i in range(0, len(b)):
    print(b[i])
    b[i] += 10  # 可修改
print(b)


# 使用while循环手动控制下标的变化
i = 0
while i < len(b):
    print(b[i])
    i += 1
