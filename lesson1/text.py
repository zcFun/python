# 输入一个人的姓名、身高、体重，求出BMI值。
#         BMI=体重（以千克为单位）2/身高（以米为单位）
# 输出，姓名、身高、体重、BMI值

x =input("输入姓名:")
y = float(input("输入身高:"))
z = float(input("输入体重:"))

BIM = z * z / y

print("BIM: %f" %BIM )



#练习二
"""
要求：能够输入姓名（3人），身高（以米为单位，精确到0.2）
体重（精确到小数点后1位），腰围（整数），输入完成以后输出以右对齐的方式对齐
"""
name = []
height = []
weight = []
waist = []
for i in range(0, 3):
    name.append(input('姓名：'))
    height.append(float(input('身高：')))
    weight.append(float(input('体重：')))
    waist.append(float(input('腰围：')))
print('{0:<10}\t{1:<10}\t{2:<10}\t{3}'.format('姓名', '身高', '体重', '腰围'))
for i in range(0, 3):
    print('{0:<10}\t{1:<10.2f}\t{2:<10.1f}\t{3:.0f}'.format(name[i], height[i], weight[i], waist[i]))