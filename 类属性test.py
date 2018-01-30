class Person(object):
    count = 0

    def __init__(self, name):
        Person.count = Person.count + 1
        self.name = name

