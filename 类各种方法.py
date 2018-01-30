# http://www.jianshu.com/p/212b6fdb2c50 （参考文档）
class Foo(object):
    """类三种方法语法形式"""
    age = 18
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls, name):
        cls.name = name
        print(cls.name)
        print(cls.age)
        print("是类方法")

    @property
    def property_method(self):
        print("属性方法")

# 实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。
# 实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
# 静态方法，参数没有要求{可以传参也可以不传参} 调用方法 （类名.方法名）名义上归类管理与实际上访问不了类或实例中的任何属性。
# 类方法，第一个参数必须要默认传类，一般习惯用cls 只能访问类变量 不能访问实例变量。
# 属性方法 把一个方法变成一个静态属性（@property) 不能传参，也不能赋值（修改方式可以实现赋值）(隐藏实现方法）
# 类方法调用
print(Foo.class_method('guo'))
# (属性方法调用）
Foo().property_method
