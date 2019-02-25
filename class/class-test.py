class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, str):
        self.my_string = str

    def hello(self):
        return 'hello world'

x = MyClass("csumb")
print(x)
print(x.my_string)
