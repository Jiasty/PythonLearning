# 使用 + 对列表进行拼接
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = b + a
print(c)
print(d)


# 使用 extend 方法,把一个列表拼接到另一个列表的后面
x = [1, 2, 3]
y = [1, 2, 3]
z = x.extend(y)
print(x)
print(y)
print(z)


# 使用 += 进行拼接
m = [1, 2, 3]
n = [4, 5, 6]
m += n
print(m)
print(n)
