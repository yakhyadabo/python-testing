import string

from src.model.person import Person


class PersonSet:

    def __init__(self) -> object:
        self.persons = set()

    def addPerson(self, person: Person):
        self.persons.add(person)

        # add list of persons, set of persons

    def add(self, name: string, age: int):
        self.persons.add(Person(name, age))

    def get(self, name: string, age: int) -> Person:
        for person in self.persons:
            if person.name == name and person.age == age:
                return person
        return None
