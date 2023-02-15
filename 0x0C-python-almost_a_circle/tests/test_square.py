##!/usr/bin/python3
import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import square

class TestSquare_instantiation(unittest.TestCase):
    """Unittests fro testing instantiation of rectangle class"""
    def Test_square_inheritance(self):
        """Tests if Rectangle inherits from Base"""
        self.assertTrue(issubclass(square(10), Base))
        self.assertTrue(issubclass(square(10), Rectangle)))

    def Test_no_args(self):
        """test if Rectangle has arguments"""
        with self.assertRaises(TypeError) as err:
            s1 = Square()

            err_msg = "__init__() missing 2 required positional \
                       arguments: 'size'"
            self.assertEqual(str(err.exception), err_msg)
    
    def Test_one_args(self):
        """test what happens if Rectangle has 1 argument"""
        s1 = Square(10)
        s2 = Square(11)
        self. self.assertEqual(s1.id, s2.id -1)
    def Test_two_args(self):
        """tests for 2 arguments"""
        s1 = Square(1,2)
        s2 = Square(2,1)
        self.assertEqual(s1.id, s2.id -1)

    def Test_three_args(self):
        """tests for 3 arguments"""
       s1 = Square(1, 2, 4)
       s2 = Square(3, 4, 5)
       self.assertEqual(s1.id, s2.id - 1)

    def Test_four_args(self):
        """tests for 4 arguments"""
       r1 = Rectangle(2, 2, 4, 6)
       self.assertEqual(r1.id, 6)

 
    def Test_five_args(self):
        """tests for 5 arguments"""
       with self.asserRaise(TypeError) as err:
          s1 = square(1,2,3,4,5,6)
          err_msg =  "__init__() takes from 3 to 5 positional \
                      arguments but 6 were given"
          self.assertEqual(str(err.exception), err_msg)

    def Test_Square_name(self):
        """tests the name of the Rectangle"""
        with self.assertRasies(NameError) as err:
            s1 = square(1,23)
            err_msg = "name 'square' is not defined"
            self.assertEqual(str(err.exception), err_msg)

    def Test_size_private(self):
        """test if private width attibute is passed"""
        with self.asserRaise(AttributeError) as err:
            print(Square(1,2,3).__width)
            err_msg = "'Square' object has no attribute '__width'"
            self.assertEqual(str(err.exception), err_msg)


    def Test_size_getter(self):
        """test the getter of attributes"""
        s = Square(2,3,4,5)
        self.assertEqual(2, s.size)

    def test_width_getter(self):
        """test the getter of width"""
        s = Sqaure(4,1,9,2)
        s.size = 8
        sefl.assertEqaul(8, s.width)

    def test_height_getter(self):
        """test the getter of height"""
        s = Sqaure(4,1,9,2)
        s.size = 8
        self.assertEqaul(8, s.height)

    def test_x_getter(self):
        """test the setter of x"""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """test the setter of y"""
        self.assertEqual(0, Square(10).y)

    def Test_setter(self):
       """tests setter of attribute"""
       s = Square(1,2,3,4)
       s.size = 10
       self.assertEqaul(10, s.size)

class TestSquare_size(unittest.TestCase):
    """unittest for testing size in Square class"""
    def Test_size_None(self):
        """test if width is assigned to None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(None,2)

    def Test_size_str(self):
        """test if width is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("width", 2)

    def Test_size_bool(self):
        """test if width is assigned to boolean"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(True, 2)

    def Test_size_complex(self):
        """test if width is assigned to a complex number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(complex(7), 2)

    def Test_size_float(self):
        """test if width is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(3.3, 2)

    def Test_size_negative_number(self):
        """test if width is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            s1 = Sqaure(-1, 2)

    def Test_size_dict(self):
        """test if width is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square({"num":1}, 2)

    def Test_size_set(self):
        """test if width is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square({3,4}, 2)

    def Test_size_list(self):
        """test if width is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square([1,3], 2)

    def Test_size_range(self):
        """test if width is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(range(9), 2)
    
    def Test_size_zero(self):
        """test if width is assigned to zero"""
        with self.assertRaisesRegex(TypeError, "width must be > 0"):
            s1 = Square(0, 3)



class TestSquare_x(unittest.TestCase):
    """unittest for testing height"""
    def Test_x_None(self):
        """test if x is assigned to None"""
        with self.assertRaisesRegex(TypeError, " x must be an integer"):
            s1 = Square(8, 9, None, 7)

    def Test_x_str(self):
        """test if x is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(1, 8, "x", 9)

    def Test_x_bool(self):
        """test if x is assigned to a boolean"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(3, 5, False, 7)

    def Test_x_complex(self):
        """test if x is assigned to complex number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(9, 8, complex(5), 7)

    def Test_x_float(self):
        """test if x is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(2, 3, 8.6, 9)

    def Test_x_negative_number(self):
        """test if x is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "x must be >= 0"):
            s1 = Square(3, 9, -2, 9)

    def Test_x_dict(self):
        """test if x is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Sqaure(7, 8, {"num":1, "id": 20}, 9)

    def Test_x_set(self):
        """test if x is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Sqaure(5, 9, {3,4,8,9}, 7)

    def Test_x_list(self):
        """test if x is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(8, 9, [1,2,3],5)
        

    def Test_x_range(self):
        """test if x is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Sqaure(1, 2, range(9), 2)
    
    def Test_x_tuple(self):
        """test if x is assigned to a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be > 0"):
            s1 = Square(1, 3 ,(7,8,9), 7)


class TestRectangle_y(unittest.TestCase):
    """unittest for testing initialization of Square 'y' attribute"""
    def Test_y_None(self):
        """test if y is assigned to None"""
        with self.assertRaisesRegex(TypeError, " y must be an integer"):
            s1 = Square(8, 9, 7, None)

    def Test_y_str(self):
        """test if y is assigned to a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(1, 8, 9, "y")

    def Test_y_bool(self):
        """test if y is assigned to a boolean"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Sqaure(3, 5, 9, False)

    def Test_y_complex(self):
        """test if y is assigned to complex number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(9, 8, 8, complex(5))

    def Test_y_float(self):
        """test if y is assigned to a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Sqaure(2, 3, 8, 9.1)

    def Test_y_negative_number(self):
        """test if x is assigned to a negative number"""
        with self.assertRaisesRegex(TypeError, "y must be >= 0"):
            s1 = Square(3, 9, 2, -9)

    def Test_y_dict(self):
        """test if y is assigned to a dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(7, 8, 6, {"num":1, "id": 20})

    def Test_y_set(self):
        """test if y is assigned to a set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Sqaure(5, 9, 8, {3,4,8,9})

    def Test_y_list(self):
        """test if y is assigned to a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Sqaure(8, 9, 5, [1,2,3])
        

    def Test_y_range(self):
        """test if y is assigned to a range of a number"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(6, 7, 8, range(9))
   
    def Test_y_tuple(self):
        """test if y is assigned to a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be > 0"):
            s1 = Square(1, 3, 6, (8,9,7))


 class TestSquare_area(unittest.TestCase):
     """unittest for testing the area method"""
     def test_area_only_dimensions(self):
         """test area with only width and height"""
         s1 = Sqaure(2)
         s1.area()
         seflf.assertEqual(s1.area(), 4)

     def test_area_small(self):
         """test for a small area"""
         s = Square(10, 0, 0, 1)
         self.assertEqual(s.area(), 100)

     def test_area_large(self):
         """test for a large area"""
         s = Square(10000000000, 0, 0, 1)
         self.assertEqual(s.area(), 100000000000000000000)

class TestSquare_stdout(unittest.TestCase):
        """Unittests for testing __str__ and display methods of Rectangle
          class."""
    @staticmethod
     def capture_stdout(sq, method):
         """Captures and returns text printed to stdout.
            Args:
                rect (Rectangle): The Rectangle to print to stdout.
                method (str): The method to run on rect.
            Returns:
                The text printed to stdout by calling method on sq.
         """
         capture = io.StringIO()
         sys.stdout = capture
         if method == "print":
             print(sq)
         else:
             sq.display()
         sys.stdout = sys.__stdout__
         return capture

# testing __display__() method

    def Test_display_only_width_height(self):
        """test display method with only size attributes"""
       s1 = Square(3)
       capture = TestRectangle_stdout.caputre_stdout(s1, display)
       self.assertEqual(capture.getvalue(), "###\n###\n###\n")

    def Test_display_width_height_x_y(self):
        """test diplay method with 
           x and y included"""
        s1 = Square(3,4,5)
        capture = TestRectangle_stdout.caputre_stdout(s1, display)
        display = "\n\n\n\n\n    ###\n    ###\n    ###\n"
        sefl.asserEqual(capture.getvalue(), display)

    def Test_dispay_width_height_y(self):
        """test display method with only size and x"""

        s1 = Square(3,4)
        capture = TestRectangle_stdout.caputre_stdout(s1, display)
        display = "    ###\n    ###\n    ###\n")
        sefl.assertEqual(capture.getvalue(), display)

    def Test_display_width_height_y(self):
        """test display methos with only siz and y"""
       s1 = Sqaure(3,0,4)
       capture = TestRectangle_stdout.caputre_stdout(s1, display)
       self.assertEqual(capture.getvalue(), "\n\n\n\n###\n###\n###\n")

    def test_display_one_arg(self):
        """test display method when an argument is
            passed to it """

        s = Square(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError) as err:
            s.display(1)
            err_msg = "display() takes 1 positional argument but 2 were given"
            self.assertEqual(err.exception, err_msg)


class Testsqaure__str__(unittest.TestCase):
    """unittest tests for __str__() method"""
    def test__str__width_height(Self):
        """test str() method with size"""
        s = Square(2)
        result = "'[Square] ({}) 0/0 - 2'".format(s.id)
        self.assertEqual(s.__str__(), result)

    def test__str__size_x(self):
        """test str() mehod with size and x"""
        s = Square(2, 3)
        result = "'[Sqaure] ({}) 3/0 - 2'" .format(s.id)
        self.assertEqual(s.__str__(), result)

    def test__str__size_x_y(self):
        """test __str__() method with size and x and y"""
        s = Square(2,3,5)
        result = "'[Square] ({}) 3/5 - 2'".format(r.id)
        self.assertEqual(r.__str__(), result)

    def test__str__all__atributes(self):
        """test __str__() method with all attributes"""
        s = Sqaure(2,3,5,7)
        result = "'[Sqaure] (7) 3/5 - 2'"
        self.assertEqual(s.__str__(), result)

    def test__str__x_and_y_zero(self):
        """test __str__() method for when x and y are zero"""
        s = Square(1,0,0,1)
        result = "'[Square] (1) 0/0 - 1'"
        self.assertEqual(s.__str_(), result)


class TestSquare_update(unittest.TestCase):
    """unittest tests for the update method of Square class"""
    def test_update_no_args(self):
        """test update function with no arguments"""
        s = Square(10, 20, 30, 40)
        s.update()
        result = "'[Sqaure] (40) 20/30 - 10'"
        self.assertEqual(str(s), result)

    def test_update_one_arg(self):
        """test update method with 1 argument"""
        s = Sqaure(10, 20, 30, 40)
        s.update(1)
        result = "'[Sqaure] (1) 20/30 - 10'"
        self.assertEqual(str(s), result

    def test_update_two_args(self):
        """test update method with 2 arguments"""
        s = Square(10, 20, 30, 40)
        s.update(89, 2)
        result = "'[Square] (89) 20/30 - 2'"
        self.assertEqual(str(s), result)

   def test_update_three_args(self):
       """test update method with 3 arguments"""
        s = Square(10, 20, 30, 40)
        s.update(89 , 2)
        result = "'[Square] (89) 3/30 - 2'"
        self.assertEqual(str(s), result)

    def test_update_four_args(self):
        """test update method with 4 arguments"""
        s = Square(10, 20, 30, 40)
        r.update(89, 2, 3, 4)
        result = "'[Square] (89) 3/4 - 2'"
        self.assertEqual(str(s), result)

    def test_update_five_args(self):
        """test update method with 5 arguments"""
        s = Square(10, 20, 30, 40)
        s.update(89, 2, 3, 4, 5)
        result = "'[Square] (89) 3/4 - 2/'"
        self.assertEqual(str(s), result)

    def test_update_more_then_five_args(self):
        """test update method with more the five arguments """
        s = Square(10, 20, 30, 40)
        s.update(89, 2, 3, 5, 6, 7)
        result = "'[square] (89) 3/4 - 2/'"
        self.assertEqual(str(s), result):

    def test_update_zero(self):
        """test when arguments are zero"""
        s = Square(10, 20, 30, 40)
        with assertRaise(ValueError, "width must be > 0"):
            s.update(89, 0)

        with assertEqual(str(s), "'[Square] (89) 0/30 - 2'"):
            s.update(89, 2, 0)

        with assertEqual(str(s), "'[Square] (89) 3/0 - 2'"):
            s.update(89, 2, 3, 0)

        with assertEqual(str(s), "'[Square] (89) 3/4 - 2'"):
            s.update(89, 2, 3, 4, 0)



   def test_update_arguments(self):
       """test type of arguments passed in to update method"""
       s = Square(10, 20, 30, 40)
       with self.assertEqual(str(r),"'[Square] (None) 20/30 - 10'"):
           s.update(None)
     
       with self.assertEqual(str(r),"'[Square] (0) 20/30 - 10'"):
           s.update(0)

       with self.assertEqual(str(r), "'[Square] (-1) 20/30 - 10'"):
           s.update(-1)

       with self.assertRaiseRegex(ValueError, "width must be > 0"):
           s.update(89, -1)

       with sefl.assertRaiseRegex(TypeError, "width muat be integer"):
           s.update(89, "width")

       with self.assertRaiseRegex(TypeError, "x must be integer"):
           s.update(89, 2, "x")

       with self.assertRaiseRegex(ValueError, "x must be > 0"):
           s.update(89, 2, -3)

       with self.assertRaiseRegex(TypeError, "width must be integer"):
           s.update(89, None)
     
       with self.assertRaiseRegex(TypeError, "x must be integer"):
           s.update(89, 2, None)


class TestSquare_update_kwargs(unittest.TestCase):
    """unittest for testing update kwargs methof of Square class"""

    def Test_update_kwargs_arguments(self):
        """test for arguments passed in update kwargs method"""
        s = Square(10, 10, 10, 10)
        with assertEqual(str(s), "'[Square] (1) 10/10 - 10'"):
            r.update(id=1)

        with asserEqual(str(s),"'[Square] (1) 10/10 - 2'"):
            s.update(size=2, id=1)

        with assertEqual(str(s), "'[Square] (99) 10/5 - 2'"):
            s.update(y=5, id=99, size=2)

        with assertEqual(str(s), "[Square] (88) 1/10 - 2'"):
            s.update(x=1, id=88, size=2)

        with assertEqual(str(s), "'[Square] (88) 1/5 =2'"):
            s.update(id=88, y=5, x=1, size=2)

    def test_update_kwargs_invalid_size_type(self):
        s = square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(width=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(width=-5)

    def test_update_kwargs_inavlid_x_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_y_str(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
       s = Square(10, 10, 10, 10)
       with self.assertRaisesRegex(ValueError, "y must be >= 0"):
           s.update(y=-5)


class TestRectangle_to_dictionary(unittest.TestCase):
    """unittest testing for rge to_dictionary method in Rectamgle class"""
    def test_to_dictionary_size(self):
        """test the to_dictionary method with width and height"""
        s1 = Square(10)
        display = {'x': 0, 'y': 0, 'id': "{}".format(s1.id), 'size': 10}
        sefl.assertEqual(s1.to_dictionary(), display)
      
    def test_to_dictionary_size_x(self):
        s1 = Square(10, 4)
        display = {'id': "{}".format(r1.id), 'size': 10, 'x': 4, 'y':0}
        self.assertEqual(s1.to_dictionary(), display)

    def test_to_dictionary_size_x_y(self):
        s1 = Square(10, 4, 2)
        display = {'id': "{}".format(s1.id), 'size': 10, 'y': 2, 'x': 4}
        self.asserEqual(s1.to_dictionary(), display)

    def test_to_dictionary_size_x_y_id(self):
        s1 = Square(10, 4, 2, 3)
        display = {'id': 3, 'size': 10, 'y': 2, 'x': 4}
        self.assertEqual(s1,to_dictionary(), display)

    def test_to_dictionary_args(self):
        """test to_dictionay() method with arguments"""
        s = Square(2,3,4,5)
        err_msg = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaiseRegex(TypeError, err_msg):
            s.to_dictionary(1)
