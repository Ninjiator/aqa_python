import homeworks
import unittest

class TestHomework(unittest.TestCase):

    def test_square_area(self):
        square = homeworks.Square(4.0)

        expected_result = 16.0
        actual_result = square.area()
        self.assertEqual(expected_result, actual_result)

    def test_rectangle_area(self):
        rectangle = homeworks.Rectangle(5.0, 4.0)

        expected_result = 20.0
        actual_result = rectangle.area()
        self.assertEqual(expected_result, actual_result)

    def test_diamond_angle_b(self):
        diamond_1 = homeworks.Diamond(5,150)
        expected_result = 180 - diamond_1.get_angle_a()
        actual_result = diamond_1.get_angle_b()

        self.assertEqual(expected_result, actual_result)

    def test_student_marks(self):
        student_1 = homeworks.Student("Marko", "Polo", 28, 88)

        expected_result = 100
        student_1.set_average_mark(expected_result)
        actual_result = student_1.get_average_mark()

        self.assertEqual(expected_result, actual_result)

    def test_func_sum_of_two_numbers(self):
        a = 5
        b = 15

        expected_result = a + b
        actual_result = homeworks.sum_of_two_numbers(a,b)

        self.assertEqual(expected_result, actual_result)

    def test_func_get_an_average_number(self):
        test_list = [2,4,6]

        expected_result = sum(test_list) / len(test_list)
        actual_result = homeworks.average_in_list(test_list)
        self.assertEqual(expected_result, actual_result)

    def test_func_get_the_longest_word(self):
        test_list = ['abc', 'Oleksii', 'Mike', 'Europe']

        expected_result = test_list[1]
        actual_result = homeworks.get_the_longest_word(test_list)
        self.assertEqual(expected_result, actual_result)

    def test_func_reverse_the_string(self):
        test_string = 'helicopter'
        expected_result = test_string[::-1]
        actual_result = homeworks.reverse_the_string(test_string)
        self.assertEqual(expected_result, actual_result)

    def test_func_sum_of_even_numbers_in_list(self):
        test_list = [1,2,3,4,5,6]

        actual_result = homeworks.sum_of_even_numbers_in_list(test_list)
        expected_result = 12
        self.assertEqual(expected_result, actual_result)

    def test_func_eject_str_from_list(self):
        test_list = ['1', '2', '3', True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

        expected_result = ['1', '2', '3', 'False', '6', 'Python', 'Lorem Ipsum']
        actual_result = homeworks.eject_str_from_list(test_list)
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main(verbosity=0)
