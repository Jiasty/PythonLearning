a = 10
b = 20
c = 30
print(a < b and b < c)
print(a < b < c) # 特殊写法，更好
print(a < b and b > c)
print(a > b or b > c)
print(a < b or b > c)
print(not a < b)
print(not a > b)

# 短路求值
print(10 > 20 and 10 / 0 == 1)
print(10 < 20 or 10 / 0 == 1)