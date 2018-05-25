# 类的基本规范
- 类的命名
    - 遵循变量命名
    - 使用大驼峰命名IsBeautiful
    - 避开和系统命名相同
- 如何声明一个类
    - 必须使用class关键字
    - 类由属性和方法构成，其他的不允许出现
    - 成员属性定义可以直接只用变量赋值，如果没有可以使用None
    案例 01 class.py
    
# 实例化类
    变量 = 类名()   #实例化了一个对象
# 访问对象成员
    - 使用点操作符
    obj.成员属性方法
    obj.成员方法
# 可以通过默认内置变量检查类和对象的所有成员
    -对象所有成员检查
    obj.__dict__
    -类所有的成员   2个_
    class_name.__dict__
# 
# 
  conda list:显示anaconda安装的包
  conda env list:显示虚拟环境列表
  conda create -n xxx python=3.6 创建一个py版本为3.6的虚拟环境，名为xxx
  
 