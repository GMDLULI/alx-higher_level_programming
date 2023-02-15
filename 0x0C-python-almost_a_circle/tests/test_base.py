#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_instantiation(unittest.TestCase):
    """unittest for testing instantiation of Base class."""
    def test_no_args(self):
        """test no arguments passed"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_three_bases(self):
        """test three bases"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqaul(b1.id, b3.id -2)

    def test_one_args(self):
        """test 1 argement passed"""
        b1 = base(1)
        self.assertEqaul(b1.id, 1)

    def test_None_id(self):
        """test None argument passed"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_after_unique_id(self):
        """test id when unique id is given"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqaul(b1.id, b3.id - 1)

    def test_id_public(self):
        """test id after being declared publicly"""
        b = Base(12)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_nb_instances_private(self):
        """test if class private attribute  _nd_instance can be passed"""
        with self.assertRasies(AttributeError):
            print(Base(12).__nb_instance)

    def test_str_id(self):
        """test id as string"""
        self.assertEqual(Base("hello").id, "hello")

    def test_float_id(self):
        """test id at float"""
        self.assertEqual(Base(8.9).id, 8.9)

    def test_complex_id(self):
        """test id as complex number"""
        self.assertEqual(Base(complex(8)).id, complex(8))

    def test_bool_id(self):
        """test id as boolean"""
        self.assertEqual(Base(True).id, True)

    def test_list_id(self):
        """test id as list"""
        self.assertEqual(Base([1,2,3]).id, [1,2,3])

    def test_tuple_id(self):
        """test id as tuple"""
        self.assertEqua;(base((1,2,3)).id, (1,2,3))

    def test_dict_id(self):
        """test id as dictionary"""
        self.assertEqual(Base({"yes": 1, "no": 0}).id, {"yes": 1, "no": 0})

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBase_to_jason_string(unittest.TestCase):
    """unittest for testing to_jason_string method of base class"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
