class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"printing from parent class."

    def sayintro(self):
        print(self.name, "is", self.age, "years old.")


pers1 = Person("Shivam", 21)

pers1.sayintro()




class person1(Person):

    def __init__(self,name,age):
        super().__init__(name,age)

    def __str__(self):
        return f"{super().__str__()} {self.name} is {self.age}years old."

person11 = person1("Satyam",19)

print(person11)