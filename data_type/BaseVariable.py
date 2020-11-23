
# 因name未定义,此处直接打印将报错
# print(name)

name = "唐可馨"

print(name)

name = "Honey Tang"

print(name)

del name

# 因上面del删除了变量name,这里打印将会报错该变量未定义
# name 'name' is not defined
# print(name)

print(int('123')+123)

print(123.5+123)

# int转换小数,不会进行四舍五入
print(int(123.7))

# 先求和再转换
print(int(123.7+0.5))

print(int(round(123.4)))

# round进行了四舍五入
print(int(round(123.7)))


