"""
# 打印以下内容
* * * *
* * * *
* * * *
* * * *
"""
#方法一
print("* " * 4)
#方法二，利用for循环
for i in range(1,5):
    print("* " * 4)
#方法三：利用双层For循环
for i in range(1,5):
    #利用for循环打印一行*号
    for j  in range(0,4):
        #使用end参数控制print,end=""-不换行
        #这里打印一行*号
        print("* ",end="")
    #换行（print具有换行功能）
    print()

"""
#打印以下内容
* * * *
*     *
*     *
* * * *
"""
#思路
#1,正常利用For虚幻控制打印行
#2.如果是第一行和最后一行，完整打印
#3.否则

#外层循环控制行
for i in range(4):
    if i ==0 or i == 3:
        print("* " *4)
    if i ==1 or i == 2:
        for j in range(4):
            if j == 0 or j ==3:
                print("* ",end="")
            else:
                print("  ",end="")
        print()

for i in range(4):
    if i == 0 or i == 3:
        print("* " *4)
    if i != 0 and i != 3:
        print("*     *")

#优化上面的空心矩形
for i in  range(5):
    for j in range(6):
        if i == 0 or i == 4 or j == 0 or j == 5:
            print("*",end=" ")
        else:
            print(' ',end=" ")
    print()