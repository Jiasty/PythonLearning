a = 10
b = 15

print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)


# 字符串是对字典序比较
s1 = 'a'
s2 = 'b'
print(s1 < s2)
print(s1 > s2)
print(s1 <= s2)
print(s1 >= s2)
print(s1 == s2)
print(s1 != s2)

# 针对中文字符串比较无意义
str1 = "你好"
str2 = "哈喽"
print(str1 < str2)
print(str1 > str2)

print("###################################################")

# 浮点数误差
print(0.1 + 0.2 == 0.3)
print(0.1)
print(0.2)
print(0.1 + 0.2)


a = 0.1 + 0.2
b = 0.3
print(-0.000001 < (a - b) < 0.000001)