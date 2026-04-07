def test(a):
    print(a)


# test() 参数数量要匹配
test("asdasd")
test(11)
test(False)

def Add(x, y):
    return x + y


print(Add(10, 20))
print(Add(10.1, 20.2))
print(Add("aaa", "bbb"))
# print(Add("aaa", 10)) 也得符合语法
