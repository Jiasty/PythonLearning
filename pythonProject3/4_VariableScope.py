def getPoint():
    x = 10
    y = 20
    return x, y


# 此处的x, y不是上面函数内部的x, y
# print(x, y)


# 全局变量
a = 10

def test():
    a = 20 # 局部变量，优先
    print(f'内部{a}')


test()
print(f'外部{a}')


# 函数内部可以直接读取全局变量(局部未找到a，去全局找)
def ReadVar():
    print(a)


# 函数内部修改全局变量
def WriteVar():
    global a  # 声明a未全局
    a = 20


WriteVar()
print(a)


# if/while/for 不会影响到变量作用域
# 此时b、i都相当于全局变量
if True:
    b = 10

print(f'b = {b}')


for i in range(1, 11):
    print(i)

print(i)
