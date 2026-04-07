# 使用in/not in判定元素是否在列表中存在，返回值是布尔类型
a = [1, 2, 3, 4]
print(1 in a)
print(10 in a)
print(1 not in a)
print(10 not in a)


# 使用 index 方法, 查找元素在列表中的下标
print(f'a.index(1)对应下标: {a.index(1)}')
# print(a.index(10)) 直接抛出异常


# 使用 pop 方法删除最末尾元素
a.pop()
print(a)


# pop 按照下标来删除元素
b = [1, 2, 3, 4]
b.pop(2)
# b.pop(10)  # 越界报错
print(b)


# remove方法, 按照值删除元素
c = [1, 2, 3, 4]
c.remove(2)
# c.remove(10)  # 没有则报错
print(c)
