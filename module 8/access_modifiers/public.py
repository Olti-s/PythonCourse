class MyClass:
    def __init__(self):
        self.public_variable = "This is public variable"


    def public_method(self):
        print("This is a public method")

my_class = MyClass()

print(my_class.public_variable)
my_class.public_method()