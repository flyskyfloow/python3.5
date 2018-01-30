class Person(object):
    count = 0

    def __init__(self, name):
        Person.count = Person.count + 1
        self.__name = name

    def get_Name(self):
        return self.__name