# Upper class made for inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        
    def speak(self):
        print("I dont what know what I am saying")
        
        
# add attribute is this specific class apart from the Upper class (Pet)
# super tell what arguements we take from upper class
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
        
class Dog(Pet):    
    def speak(self):
        print("Bark")
        
class Fish(Pet):
    pass
        
p = Pet("Mike", 19)
p.speak()
c = Cat("Bill", 24, "Red")
c.show()
d = Dog("Joey", 25)
d.speak()


