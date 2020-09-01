import unittest
from linked_list import traverse_list, ListNode
from helper import counter, counted

class TestListTraverse(unittest.TestCase):
  def test_traverse_calls_callback(self):
    [get_count, count] = counter()
    count = counted(count)
    l = ListNode("190")
    traverse_list(count, l)
    self.assertEqual(count.calls, 1)

