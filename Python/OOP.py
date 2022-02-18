# OOP.py

class Human:
    def __init__(self, name, surname, age, dob, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.dob = dob
        self.job = job

    def greeting(self):
        print(f"Hi, my name is {self.name} {self.surname} and I am {self.age} years old. I was born on {self.dob} and "
              f"I work as a {self.job}")


class SuperHuman(Human):

    def __init__(self, super_power, super_hero_name, name, surname, age, dob, job):
        super().__init__(name, surname, age, dob, job)
        self.super_power = super_power
        self.super_hero_name = super_hero_name

    def super_hero_greeting(self):
        print(f"Hey, I'm {self.super_hero_name} and my power is {self.super_power}")


John, John.name, John.surname, John.age, John.dob, John.Job = Human, "John", "Doe", 24, "2/2/2222", "Software Developer"
John.greeting(John)

Joe = SuperHuman(John)

