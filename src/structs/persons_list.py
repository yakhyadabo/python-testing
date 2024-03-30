import string

from src.model.person import Person


class PersonList:

    def __init__(self):
        self.persons = list()

    def add(self, person: Person):
        self.persons.append(person)

    def get(self, name: string, age: int) -> Person:
        for person in self.persons:
            if person.name == name and person.age == age:
                return person
        return None  # TODO ???
