
# python 数据类型：数字 ，字符串，列表，元组，字典

# 输出
print('我是曾晨,来自大数据1610\n '+ 'he\'s a handsome man \n '+ '\"青出于蓝而\",出自荀子《劝学》 \n')


# 输入
x = float(input("请输入第一个数:"))
y =float(input("请输入第二个数:"))
z = float(input("请输入第三个数:"))

sum = x+ y+ z
ave = sum/3

print("三个数的和是：%f \n" %sum)

# 多行注释
""" 
# %.2f指定保留小数点后两位小数
print("三个数的平均数是：%.2f" %ave)

"""

# 缩进来表示代码块,对齐的代码表示在同一个代码块

if True:
    print("True")
else:
    print("False")
    # 表示同一个代码块
    print("False")

# 表示另外一个代码块
print("False")

# 输出语句过长通过（）来换行


# 课后测验
x =input("输入姓名")
y = float(input("输入身高"))
z = float(input("输入体重"))

BIM = z * z / y

print("BIM: %f" %BIM )