"""
Inheritance (ইনহেরিটেন্স) হলো Object-Oriented Programming (OOP)-এর একটি গুরুত্বপূর্ণ concept, যেখানে একটি class অন্য একটি class-এর properties (attributes) এবং methods (functions) inherit বা গ্রহণ করে।
"""

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()   # inherited method
d.bark()