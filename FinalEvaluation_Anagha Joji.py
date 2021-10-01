import random


class Pet:

    def _init_(self, species = None, name = ""):
        self.species = species
        self.name = name

    def species(self, m):
       m = ["dog","cat","horse","hamster"]
       for i in m:
           return True
       else:
           return "Error"

    def _str_(self):
        if len(self.name) == 0:
            print(f"Species of {self.species} ,named {self.name}")
        else:
            print(f"Species of {self.species} ,unnamed")

class Dog(Pet):

    def _init_(self,name = "", chases = "Cats"):
        self.name = name
        self.chases = chases

    def _str_(self):
        if len(self.name) == 0:
            print(f"Species of Dog, unnamed, chases {self.hates}")
        else:
             print(f"Species of Dog, named {self.name}, chases {self.hates}")


class Cat(Pet):
    def _init_(self, name="", hates="Dogs"):
        self.name = name
        self.hates = hates

    def _str_(self):
        if len(self.name) == 0:
            print(f"Species of Cat, unnamed, chases {self.hates}")
        else:
            print(f"Species of Cat, named {self.name}, chases {self.hates}")

# main functiom
m = input("Enter animal type: ")
d_name = input("Enter dog name: ")
C_name = input("Enter cat name: ")







