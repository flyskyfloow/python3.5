class Example:
    val1 = "Value 1"

    def __init__(self):
        self.val2 = "Value 2"

    @staticmethod
    def staticmd():
        print("静态方法，无法访问Value1和Value2")

    #                print(val1)

    @classmethod
    def classmd(cls):
        print('类方法，类：' + str(cls) + ",val1:" + cls.val1 + ",无法访问val2的值")
        #                print(self.val2)
        print(cls.val1)


example = Example()
example.staticmd()  # 实例调用静态方法，无法访问实例变量val1和val2
example.classmd()  # 实例调用类方法，输出结果：类方法，类：<class '__main__.Example'>,val1:Value 1,无法访问val2的值
Example.classmd()  # 类调用类方法，输出结果：类方法，类：<class '__main__.Example'>,val1:Value 1,无法访问val2的值
example.val1 = "The instance value1 changed"
example.classmd()  # 类调用类方法，输出结果：类方法，类：<class '__main__.Example'>,val1:Value 1,无法访问val2的值
Example.val1 = "The class value2 changed"
example.classmd()  # 类调用类方法，输出结果：类方法，类：<class '__main__.Example'>,val1:The class value2 changed,无法访问val2的值
Example.classmd()  # 类调用类方法，输出结果：类方法，类：<class '__main__.Example'>,val1:The class value2 changed,无法访问val2的值