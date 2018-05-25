'''
定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    pass

# 定义一个对象
weiyaojun = Student()

class PythonStudent():
    # 用None给不确定的值赋值
    # 类的属性
    name = None
    age = None
    course = "Python"

    # 与属性属于同一级缩进
    # 系统默认有一个self参数
    # 类的行为
    def DoHomework(self):
        print("我在做做作业")
        # 在函数末尾使用return
        return None
# 实例化，一个叫weiyaojun的学生，是一个具体的人
weiyaojun = PythonStudent()
print(weiyaojun.name)
print(weiyaojun.age)
print(weiyaojun.__dict__)
print(PythonStudent.__dict__)
#
weiyaojun.DoHomework()