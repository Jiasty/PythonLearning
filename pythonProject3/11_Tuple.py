# 使用()表示创建元组
a = ()
b = tuple()
print(type(a), type(b))


# 指定初始值
c = (1, 2, 3)
print(c)


# 存储任意类型
d = (1, 1.1, 'aaa', False, [], ())
print(d)

# 下标访问 []
print(c[1])


# 像读操作,比如访问下标, 切片, 遍历, in, index, + 等, 元组也是一样支持的


# 默认的集合类型tuple
def getPoint():
    return 10, 20


result = getPoint()
print(type(result))
