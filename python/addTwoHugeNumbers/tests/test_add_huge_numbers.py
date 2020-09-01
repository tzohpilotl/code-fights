import unittest
from linked_list import LinkedList, LinkedListIterator
from add_huge_numbers import add_huge_numbers

tests = [(([9876, 5432, 1999], [1, 8001]), [9876, 5434, 0])]

class TestAddHugeNumbers(unittest.TestCase):
  def test_matches_expected_results(self):
    for data, expected in tests:
      result = add_huge_numbers(LinkedList.fromList(data[0]), LinkedList.fromList(data[1]))
      result_list = [n.value for n in LinkedListIterator(result)]
      self.assertEqual(expected, result_list)