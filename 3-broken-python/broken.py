#!/usr/bun/env python

class Character:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def display():
        print(self.name + ' is ' + str(self.age) + ' years old.')

characters = [Character('Han', 30), Character('Luke', 20), Character('Leia', 20)]
for ch in characters:
    ch.display()