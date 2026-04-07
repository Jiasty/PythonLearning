# 使用open函数打开文件
f = open('./test.txt', 'r')
print(f)
print(type(f))


# 使用close方法关闭文件
f.close()


# 验证一个程序打开文件个数有限
# fs = []
# count = 0
# while True:
#     f = open('./test.txt', 'r')
#     fs.append(f)
#     count += 1
#     print(f'count = {count}')


# 写文件
f = open('./test.txt', 'w')
f.write('hello')
f.close()


# 使用 'r' 方式打开文件, 则写入时会抛出异常
# f = open('d:/test.txt', 'r')
# f.write('hello')
# f.close()


# w方式打开后清空
# f = open('./test.txt', 'w')
# f.close()

f = open('./test.txt', 'a')
f.write('world')
f.close()


# 针对已经关闭的文件对象进行写操作, 也会抛出异常
# f.write('world')


# 读文件
rf = open('./testRead.txt', 'r', encoding='utf8')
result = rf.read(2)
print(result)
rf.close()


rf = open('./testRead.txt', 'r', encoding='utf8')
for line in rf:
    print(f'line = {line}', end='')
rf.close()

rf = open('./testRead.txt', 'r', encoding='utf8')
lines = rf.readlines()
print(lines)
rf.close()

# 使用上下文管理器(很像RAII机制)
with open('./test.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    print(lines)
