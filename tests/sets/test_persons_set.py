import unittest

from src.model.person import Person
from src.structs.sets.persons_set import PersonSet


class TestPersonSet(unittest.TestCase):

    def test_add(self):
        personSet: PersonSet = PersonSet()
        personSet.add(name="John", age=20)
        ans = personSet.get(name="John", age=20)
        assert ans.name == "John" and ans.age == 20

    def test_add_person(self):
        personSet: PersonSet = PersonSet()
        personSet.addPerson(Person(name="John", age=20))
        ans = personSet.get(name="John", age=20)
        assert ans.name == "John" and ans.age == 20


if __name__ == '__main__':
    unittest.main()
