import random

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skill = 1
        self.money = 50

    def study(self):
        self.skill += 1
        self.money -= 10
        print ("Studying...")

    def chill(self):
        self.skill -= 0.5
        expenses = random.randint(25, 50)
        self.money = expenses
        print("Chilling...")

    def work(self):
        self.skill += 1
        self.money += 50
        print("Working...")

    def info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")
        print(f"Skills: {self.skill}")
        print(f"Money: {self.money}")

alex = Student("Alex", 15)
alex.info()

for day in range(366):
    choice = random.randint(0,2)

    if choice == 0:
        alex.chill()
    elif choice == 1:
        alex.work()
    else:
        alex.study()


alex.age += 1
alex.info()