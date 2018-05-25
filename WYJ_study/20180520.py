#打印一个直角三角形
for i in range(5):
    for j in range(i,5):
        print("* ",end="")
    print()

#九九乘法表
#方法一
for i in range(1,10):
    for j in range(1,i+1):
        # %d整型格式化输出， %-2d   -表示左对齐，2表示不足两位不齐，用空格补齐" "
        print(" ".join(["%dX%d=%-2d" % (i, j, j * i) ]),end=" ")
    print()


#方法二
for i in range(10):
    print(" ".join(["%dX%d=%-2d"%(m,i,m*i) for m in range(1,i+1)]))
