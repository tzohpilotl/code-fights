import unittest
from linked_list import ListNode, shift_list, length

class TestShiftList(unittest.TestCase):
  def test_lenght_grows(self):
    l = ListNode('1')
    self.assertEqual(length(l), 1)
    l = shift_list(ListNode('0'), l)
    self.assertEqual(length(l), 2, 'Length should grow by 1')
  
  def test_nodes_are_ordered(self):
    l = ListNode('1')
    self.assertEqual(l.value, '1')
    l = shift_list(ListNode('0'), l)
    self.assertEqual(l.value, '0', 'Current node should have latest value')
