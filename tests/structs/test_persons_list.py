import unittest

from src.model.person import Person
from src.structs.persons_list import PersonList


class TestPersonList(unittest.TestCase):

    # def test_add(self):
    #     personList: PersonList = PersonList()
    #     personList.add(name="John", age=20)
    #     ans = PersonList.get(name="John", age=20)
    #     assert ans.name == "John" and ans.age == 20

    def test_add_person(self):
        person_list: PersonList = PersonList()
        person_list.add(Person(name="John", age=20))
        ans = person_list.get(name="John", age=20)
        assert ans.name == "John" and ans.age == 20


if __name__ == '__main__':
    unittest.main()
