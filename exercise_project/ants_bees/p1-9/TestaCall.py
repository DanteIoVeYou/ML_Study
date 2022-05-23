class Person:
    def __call__(self, name):
        print("__call__"+"hello"+name)

    def hello(self, name):
        print("hello"+name)

person = Person()
person.__call__("zhangsan")
person("Zhangsan")
person.hello("lisi")
person()