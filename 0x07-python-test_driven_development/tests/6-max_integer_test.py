#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_equal(self):
        """Test if element of the list are equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_none(self):
        """Test if empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_char(self):
        """Test if list elements are character characters."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_max_at_beginning(self):
        """Test max at beginning."""
        self.assertEqual(max_integer([4, 3, 3]), 4)

    def test_max_at_middle(self):
        """Test max at the middle."""
        self.assertEqual(max_integer([3, 4, 3]), 4)

    def test_list_of_one_element(self):
        """Test list of one element."""
        self.assertEqual(max_integer([3]), 3)
