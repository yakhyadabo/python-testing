import string

from src.model.person import Person


class PersonDict:

    def __init__(self):
        self.persons = dict()

    def add(self, person: Person):
        self.persons[person.pid] = person

    def get(self, pid: int) -> Person:
        return self.persons.get(pid)

    def remove(self, pid: int) -> Person:
        return self.persons.pop(pid)
