import unittest

from src.model.person import Person
from src.structs.persons_dict import PersonDict


class TestPersonDict(unittest.TestCase):

    def test_add_person(self):
        person_dict: PersonDict = PersonDict()
        person = Person(name="John", age=20)
        person_dict.add(person)
        ans = person_dict.get(person.pid)
        assert ans.name == "John" and ans.age == 20


if __name__ == '__main__':
    unittest.main()
