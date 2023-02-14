##!/usr/bin/python3
import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base
from contextlib import redirect_stdout

class TestRectangle_instantiation(unittest.TestCase):
    """Unittests fro testing instantiation of rectangle class"""
    def Test_rectangle_inheritance(self):
        """Tests if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def Test_no_args(self):
        """test if Rectangle has arguments"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle()

            err_msg = "__init__() missing 2 required positional \
                       arguments: 'width and 'height'"
            self.assertEqual(str(err.exception), err_msg)
    
    def Test_one_args(self):
        """test what happens if Rectangle has 1 argument"""
       with self.assertRaises(TypeError) as err:
           r2 = Rectangle(1)
           err_msg = " __init__() missing 1 required positional \
               argument: 'height'"
           self.assertEqual(str(err.exception), err_msg)

    def Test_two_args(self):
        """tests for 2 arguments"""
        r1 = Rectangle(1,2)
        r2 = Rectangle(2,1)
        with self.assertEqual(r1.id, r2.id -1)

    def Test_three_args(self):
        """tests for 3 arguments"""
       r1 = Rectangle(1, 2, 4)
       r2 = Rectangle(3, 4, 5)
       with self.assertEqual(r1.id, r2.id - 1)

    def Test_four_args(self):
        """tests for 4 arguments"""
       r1 = Rectangle(2, 2, 4, 6)
       r2 = Rectangle(8, 9, 5, 7)
       with self.assertEqual(r1.id, r2.id - 1)

    def Test_five_args(self):
        """tests for 5 arguments"""
       r1 = Rectangle(7, 8, 3, 4, 1)
       r2 = Rectangle(3, 4, 5, 6, 7)
       with self.assertEqual(r1.id, r2.id - 1)

    def Test_more_then_five_args(self):
        """tests for more then 5 arguments"""
       with self.asserRaise(TypeError) as err:
          r1 = Rectangle(1,2,3,4,5,6)
          err_msg =  "__init__() takes from 3 to 6 positional \
                      arguments but 7 were given"
          self.assertEqual(str(err.exception), err_msg)

    def Test_Rectangle_name(self):
        """tests the name of the Rectangle"""
        with self.assertRasies(NameError) as err:
            r1 = rectangle(1,23)
            err_msg = "name 'rectangle' is not defined"
            self.assertEqual(str(err.exception), err_msg)

    def Test_width_private(self):
        """test if private width attibute is passed"""
        with self.asserRaise(AttributeError) as err:
            print(Rectangle(1,2,3).__width)
            err_msg = "'Rectangle' object has no attribute '__width'"
            self.assertEqual(str(err.exception), err_msg)


    def Test_height_private(self):
        """test if private height attibute is passed"""
        with self.asserRaise(AttributeError) as err:
            print(Rectangle(7,9).__height)
            err_msg = "'Rectangle' object has no attribute '__height'"
            self.assertEqual(str(err.exception), err_msg)


    def Test_x_private(self):
        """test if private x attibute is passed"""
        with self.asserRaise(AttributeError) as err:
            print(Rectangle(1,2,3).__x)
            err_msg = "'Rectangle' object has no attribute '__x'"
            self.assertEqual(str(err.exception), err_msg)

    def Test_y_private(self):
        """test if private y attibute is passed"""
        with self.asserRaise(AttributeError) as err:
            print(Rectangle(1,2,3,9).__y)
            err_msg = "'Rectangle' object has no attribute '__y'"
            self.assertEqual(str(err.exception), err_msg)

   def Test_getter(self):
       """test the getter of attributes"""
       r = Rectangle(2,3,4,5)
       self.assertEqual(2, r.width)
       self.asserEqual(3, r.height)
       self.assertEqual(4, r.x)
       self.assertEqual(5, r.y)

   def Test_setter(self):
       """tests setter of attribute"""
       r = Rectangle(1,2,3,4)
       r.width = 10
       self.assertEqaul(10, r.width)

       r.height = 90
       self.assertEqual(90, r.height)
       
       r.x = 16
       self.assertEqual(16, r.x)

       r.y = 40
       self.assertEqual(40, r.y)

class TestRectangle_width(unittest.TestCase):
    """unittest for testing width"""
    def Test_width_None(self):
        """test if width is assigned to None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(None,2)

    def Test_width_str(self):
        """test if width is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle("width", 2)

    def Test_width_bool(self):
        """test if width is assigned to boolean"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(True, 2)

    def Test_width_complex(self):
        """test if width is assigned to a complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(complex(7), 2)

    def Test_width_float(self):
        """test if width is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(3.3, 2)

    def Test_width_negative_number(self):
        """test if width is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r1 = Rectangle(-1, 2)

    def Test_width_dict(self):
        """test if width is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({"num":1}, 2)

    def Test_width_set(self):
        """test if width is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle({3,4}, 2)

    def Test_width_list(self):
        """test if width is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle([1,3], 2)

    def Test_width_range(self):
        """test if width is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(range(9), 2)
    
    def Test_width_zero(self):
        """test if width is assigned to zero"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r1 = Rectangle(0, 3)



class TestRectangle_height(unittest.TestCase):
    """unittest for testing height"""
    def Test_height_None(self):
        """test if height is assigned to None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(8, None)

    def Test_height_str(self):
        """test if height is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(1, "height")

    def Test_height_bool(self):
        """test if height is assigned to a boolean"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(3, False)

    def Test_height_complex(self):
        """test if height is assigned to complex number"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(9, complex(5))

    def Test_height_float(self):
        """test if height is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(2, 5.6)

    def Test_height_negative_number(self):
        """test if height is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "height must be > 0"):
            r1 = Rectangle(3, -2)

    def Test_height_dict(self):
        """test if height is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(7, {"num":1, "id": 20})

    def Test_height_set(self):
        """test if height is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(5, {3,4,8,9})

    def Test_height_list(self):
        """test if height is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(5, [1,3,9])


    def Test_height_range(self):
        """test if height is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1 = Rectangle(7, range(9))

    def Test_width_range(self):
        """test if width is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1 = Rectangle(range(9), 2)
    
    def Test_width_zero(self):
        """test if width is assigned to zero"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            r1 = Rectangle(0, 3)


class TestRectangle_x(unittest.TestCase):
    """unittest for testing height"""
    def Test_x_None(self):
        """test if x is assigned to None"""
        with self.assertRaisesRegex(TypeError, " x must be an integer"):
            r1 = Rectangle(8, 9, None, 7)

    def Test_x_str(self):
        """test if x is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(1, 8, "x", 9)

    def Test_x_bool(self):
        """test if x is assigned to a boolean"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(3, 5, False, 7)

    def Test_x_complex(self):
        """test if x is assigned to complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(9, 8, complex(5), 7)

    def Test_x_float(self):
        """test if x is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(2, 3, 8.6, 9)

    def Test_x_negative_number(self):
        """test if x is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            r1 = Rectangle(3, 9, -2, 9)

    def Test_x_dict(self):
        """test if x is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(7, 8, {"num":1, "id": 20}, 9)

    def Test_x_set(self):
        """test if x is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(5, 9, {3,4,8,9}, 7)

    def Test_x_list(self):
        """test if x is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 - Rectangle(8, 9, [1,2,3],5)
        

    def Test_x_range(self):
        """test if x is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1 = Rectangle(1, 2, range(9), 2)
    
    def Test_x_tuple(self):
        """test if x is assigned to a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be > 0")
        r1 = Rectangle(1, 3 ,(7,8,9), 7)


class TestRectangle_y(unittest.TestCase):
    """unittest for testing height"""
    def Test_y_None(self):
        """test if y is assigned to None"""
        with self.assertRaisesRegex(TypeError, " y must be an integer"):
            r1 = Rectangle(8, 9, 7, None)

    def Test_y_str(self):
        """test if y is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(1, 8, 9, "y")

    def Test_y_bool(self):
        """test if y is assigned to a boolean"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(3, 5, 9, False)

    def Test_y_complex(self):
        """test if y is assigned to complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(9, 8, 8, complex(5))

    def Test_y_float(self):
        """test if y is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(2, 3, 8, 9.1)

    def Test_y_negative_number(self):
        """test if x is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            r1 = Rectangle(3, 9, 2, -9)

    def Test_y_dict(self):
        """test if y is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(7, 8, 6, {"num":1, "id": 20})

    def Test_y_set(self):
        """test if y is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(5, 9, 8, {3,4,8,9})

    def Test_y_list(self):
        """test if y is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(8, 9, 5, [1,2,3])
        

    def Test_y_range(self):
        """test if y is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1 = Rectangle(6, 7, 8, range(9))
    
    def Test_y_tuple(self):
        """test if y is assigned to a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be > 0")
        r1 = Rectangle(1, 3, 6, (8,9,7))


 class TestRectangle_area(unittest.TestCase):
     """unittest for testing the area method"""
     def test_area_only_dimensions(self):
         """test area with only width and height"""
         r1 = Rectangle(2, 9)
         r1.area()
         seflf.assertEqual(r1.area(), 18)

     def test_area_all_arguments(self):
         """test area() with all postional arguments"""
         r1 = Rectangle(8, 9, 6, 11 3)
         r1.area()
         self.assertEqual(r1.area(), 72)

     def test_area_changed_atributes(self):
         """test ares() with changing attributes"""
         r1 = Rectangle(1,2,3,4,5)
         r.width = 7
         r.height = 8
         self.assertEqual(r.area(), 56)

     def test_area_small(self):
         """test for a small area"""
         r = Rectangle(10, 3, 0, 0, 0)
         self.assertEqual(r.area(), 30)

     def test_area_large(self):
         """test for a large area"""
         r = Rectangle(10000000000, 10000000000, 0, 0, 1)
         self.assertEqual(r.area(), 100000000000000000000)
