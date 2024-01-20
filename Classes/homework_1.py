import unittest


class Rectangle:

    def __init__(self, *args):

        if len(args) == 2:
            self._a = args[0]
            self._b = args[1]
        elif len(args) == 1:
            self._a = args[0]
            self._b = 5
        elif len(args) == 0:
            self._a = 4
            self._b = 3
        else:
            raise ValueError("Wrong argument!")

    def get_side_a(self):
        return self._a

    def set_side_a(self, a):
        self._a = a

    def get_side_b(self):
        return self._b

    def set_side_b(self, b):
        self._b = b

    def side_a(self, a=None):
        """
        SECOND VARIANT OF GETTER AND SETTER METHOD
        """

        if a:
            self._a = a
        return self._a

    def side_b(self, b=None):
        """
        SECOND VARIANT OF GETTER AND SETTER METHOD
        """
        if b:
            self._b = b
        return self._b

    def area(self):
        return self._a * self._b

    def perimeter(self):
        return 2 * (self._a + self._b)

    def is_square(self):
        return self._a == self._b

    def replace_sides(self):
        replaced_side = self._b
        self._b = self._a
        self._a = replaced_side


class ArrayRectangles:
    rectangle_array = []

    def __init__(self, *args):
        """
        1. Constructor creating an empty array of rectangles with length n
        2. Constructor that receives an arbitrary amount of objects of type Rectangle
        """

        if isinstance(args[0], int):
            self._rectangle_array = [None] * args[0]
        elif isinstance(args[0], Rectangle):
            self._rectangle_array = list(args)

    def add_rectangle(self, rectangle: Rectangle):
        """
            If RECTANGLE_ARRAY is created with Constructor creating an empty array of rectangles with length n
            -> it returns TRUE till NONE values are present

            If RECTANGLE_ARRAY is created with Constructor that receives an arbitrary amount of objects of type
            Rectangle -> it returns FALSE, because the size of such array is defined by amount of already existent
            objects inside
        """
        for i in range(0, len(self._rectangle_array)):
            if self._rectangle_array[i] is None:
                self._rectangle_array[i] = rectangle
                return True
        return False

    def number_max_area(self):
        """
        return INDEX of rectangle with maximum area

        If NULL values are present in array, the error will be raised
        """
        results_areas = []
        for i in self._rectangle_array:
            if i is None:
                raise AttributeError("Array of Rectangles has null value!")
            results_areas.append(i.area())
        return results_areas.index(max(results_areas))

    def number_min_perimeter(self):
        """
        return INDEX of rectangle with minimal perimeter

        If NULL values are present in array, the error will be raised
        """
        results_perimeters = []
        for i in self._rectangle_array:
            if i is None:
                raise AttributeError("Array of Rectangles has null value!")
            results_perimeters.append(i.perimeter())
        return results_perimeters.index(min(results_perimeters))

    def number_square(self):
        """
        returns AMOUNT of squares in array

        If NULL values are present in array, the error will be raised
        """
        count = 0
        for i in range(0, len(self._rectangle_array)):
            if self._rectangle_array[i].is_square():
                count = count + 1
        return count


class RectangleTests(unittest.TestCase):

    def tests_rectangles(self):
        rectangle_1 = Rectangle(4, 4)
        rectangle_2 = Rectangle(5, 6)
        rectangle_3 = Rectangle(7, 8)
        rectangles = ArrayRectangles(2)

        self.assertTrue(rectangles.add_rectangle(rectangle_1))
        self.assertTrue(rectangles.add_rectangle(rectangle_2))
        self.assertFalse(rectangles.add_rectangle(rectangle_3))  # FALSE -> because defined size is 2,
        # and that's why no place for 3rd rectangle

        rectangles_2 = ArrayRectangles(rectangle_1, rectangle_2, rectangle_3)
        self.assertFalse(rectangles_2.add_rectangle(rectangle_1))  # FALSE -> because the size is defined by already
        # added elements

        self.assertEqual(rectangles_2.number_max_area(), 2)  # 2 - return INDEX of rectangle with max area
        self.assertEqual(rectangles_2.number_min_perimeter(), 0)  # 0 - return INDEX of rectangle with min area
        self.assertEqual(rectangles_2.number_square(), 1)  # 1 - return AMOUNT of squares in array

        rectangles_3 = ArrayRectangles(1)
        with self.assertRaises(AttributeError, msg="Array of Rectangles has null value!"):
            rectangles_3.number_min_perimeter()


if __name__ == '__main__':
    unittest.main()