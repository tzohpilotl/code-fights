import unittest
from linked_list import ListNode, last_of_list, shift_list

class TestLastOfList(unittest.TestCase):
  def test_it_returns_the_correct_node(self):
    l = ListNode('1')
    last = last_of_list(l)
    self.assertEqual(last.value, '1')
    l = shift_list(ListNode('0'), l)
    last = last_of_list(l)
    self.assertEqual(last.value, '1')