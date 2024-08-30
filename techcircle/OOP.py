class Dog:
    species = "Canis familiars"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
        
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Car:
    wheels =  4

    def __init__(self, color, model):
        self.color = color
        self.model = model


myDog = Dog("Buddy", 3)

print(myDog.name)
print(myDog.age)

print(myDog.description())
print(myDog.speak("Woof"))