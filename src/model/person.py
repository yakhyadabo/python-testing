import string


class Person:

    def __init__(self, name: string, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def __repr__(self):
        return f"SetObject ({self.name} {self.age} (id: {id(self)}"

    def __hash__(self):
        return hash((self.name + str(self.age)))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.name == other.name and self.age == other.age

    # def __cmp__(self, other):
    #     # check the names
    #     if self.name > other.name: return 1
    #     if self.name < other.name: return -1
    #     # names are the same...
    #     # check ages
    #     if self.age > other.age: return 1
    #     if self.age < other.age: return -1
    #     # age are the same...
    #     # it's a tie
    #     return 0
