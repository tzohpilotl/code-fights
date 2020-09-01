import unittest
from helper import counter

class TestCounter(unittest.TestCase):
  def test_counter_adds(self):
    [get, add] = counter()
    # Should be 0
    self.assertAlmostEqual(get(), 0)
    # Add 1
    add()
    self.assertEqual(get(), 1)

