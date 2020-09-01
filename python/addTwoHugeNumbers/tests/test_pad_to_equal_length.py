import unittest
from linked_list import ListNode, pad_to_equal_length, length

class TestPadToEqualLength(unittest.TestCase):
  def test_resulting_list_has_desired_length(self):
    l = ListNode('1')
    l = pad_to_equal_length(5, l)
    self.assertEqual(length(l), 5)

