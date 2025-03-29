class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
student1=student("John",20)
student1.display()
student3=student("Bob",21)
student3.display()