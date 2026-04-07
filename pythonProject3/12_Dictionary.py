# 创建字典
a = {}
b = dict()
print(type(a), type(b))


# 初始化
# c = {'id': 1, 'name': 'Jiasty'}
c = {
    'id': 1,
    'name': 'Jiasty'
}
print(c)


# 查找
print('id' in c)
print(1 in c)
print(c['name'])
# print(c[100])  异常


# 新增、修改键值对
c['score'] = 315  # 此处是写操作，并非查询
print(c)

c['score'] = 400  # 此处是写操作，并非查询
print(c)


# pop删除键值对
c.pop('score')
print(c)


# 遍历
student = {
    'id': 1,
    'name': 'zhangsan',
    'score': 80
}
for key in student:
    print(key, student[key])

print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

# 可hash类型
print(hash(0))
print(hash(3.14))
print(hash('hello'))
print(hash(True))
print(hash(()))  # 元组可hash
# 列表和字典不可hash
# print(hash([1, 2, 3]))
# print(hash({ 'id': 1 }))
