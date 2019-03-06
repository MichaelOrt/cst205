class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, str):
        self.my_string = str

    def hello(self, name):
        print ("hello" + name)
        return 'hello world'

    def give_up_string(self):
        print(self.my_string)

x = MyClass("csumb")
print(x)
print(x.my_string)
x.give_up_string
