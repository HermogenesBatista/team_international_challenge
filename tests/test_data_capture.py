import unittest

from data_capture import DEFAULT_LIMITS
from data_capture import DataCapture
from data_capture.exceptions import DataCaptureValueError
from . import DEFAULT_DATA_ERROR_TYPES, DEFAULT_DATA_ERROR_lIMITS


class TestDataCapture(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set Default data test
        """
        cls.capture = DataCapture()
        cls.capture.add(3)
        cls.capture.add(9)
        cls.capture.add(3)
        cls.capture.add(4)
        cls.capture.add(6)

    def test_add_values(self):
        """
        Test insert correct value type and between limits
        """
        capture = DataCapture()
        test_correct_values = [0, 4, 6, 10, 100, 150, 500, 999, 1000]
        for value in test_correct_values:
            capture.add(value)

    def test_add_values_validation_limits_error(self):
        """
        Test values between limits when add values.
        """
        for value in DEFAULT_DATA_ERROR_lIMITS:
            with self.assertRaises(DataCaptureValueError) as except_info:
                self.capture.add(value)
            self.assertEqual(
                f"The values must be between: {DEFAULT_LIMITS}",
                str(except_info.exception)
            )

    def test_add_values_validation_type_validation_error(self):
        """
        Test type of data is correct when add values.
        """
        for type_, value in DEFAULT_DATA_ERROR_TYPES:
            with self.assertRaises(DataCaptureValueError) as except_info:
                self.capture.add(value)
            self.assertEqual(
                f"Only integer is allowed. Found: {type_}",
                str(except_info.exception)
            )

    def test_less_values(self):
        """
        Test count occurrences that are lower than given number.
        """
        stats = self.capture.build_stats()
        self.assertEqual(2, stats.less(4))
        self.assertEqual(0, stats.less(3))
        self.assertEqual(3, stats.less(6))
        self.assertEqual(4, stats.less(9))
        self.assertEqual(5, stats.less(10))

    def test_less_values_validation_outside_limit(self):
        """
        Test raise error in case of lower or greater than limits.
        """
        stats = self.capture.build_stats()
        for value in DEFAULT_DATA_ERROR_lIMITS:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.less(value)
            self.assertEqual(
                f"The values must be between: {DEFAULT_LIMITS}",
                str(except_info.exception)
            )

    def test_less_values_validation_type_validation_error(self):
        """
        Test raise error in case of wrong type.
        """
        stats = self.capture.build_stats()
        for type_, value in DEFAULT_DATA_ERROR_TYPES:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.less(value)
            self.assertEqual(
                f"Only integer is allowed. Found: {type_}",
                str(except_info.exception)
            )

    def test_greater_values(self):
        """
        Test count occurrences that are greater than given number.
        """
        stats = self.capture.build_stats()
        self.assertEqual(stats.greater(0), 5)
        self.assertEqual(stats.greater(2), 5)
        self.assertEqual(stats.greater(3), 3)
        self.assertEqual(stats.greater(4), 2)
        self.assertEqual(stats.greater(7), 1)
        self.assertEqual(stats.greater(8), 1)
        self.assertEqual(stats.greater(9), 0)
        self.assertEqual(stats.greater(10), 0)

    def test_greater_values_validation_outside_limit(self):
        """
        Test raise error in case of lower or greater than limits.
        """
        stats = self.capture.build_stats()
        for value in DEFAULT_DATA_ERROR_lIMITS:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.greater(value)
            self.assertEqual(
                f"The values must be between: {DEFAULT_LIMITS}",
                str(except_info.exception)
            )

    def test_greater_values_validation_type_validation_error(self):
        """
        Test raise error in case of lower or greater than limits.
        """
        stats = self.capture.build_stats()
        for type_, value in DEFAULT_DATA_ERROR_TYPES:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.greater(value)
            self.assertEqual(
                f"Only integer is allowed. Found: {type_}",
                str(except_info.exception)
            )

    def test_between_values(self):
        """
        Test count occurrences that between two numbers.
        """
        stats = self.capture.build_stats()
        self.assertEqual(4, stats.between(3, 6))
        self.assertEqual(2, stats.between(4, 6))
        self.assertEqual(3, stats.between(4, 9))

        self.assertEqual(1, stats.between(7, 12))
        self.assertEqual(2, stats.between(5, 12))
        self.assertEqual(2, stats.between(12, 5))

        self.assertEqual(5, stats.between(0, 9))
        self.assertEqual(5, stats.between(9, 0))

    def test_between_values_outside_limit(self):
        """
        Test raise error in case of lower or greater than limits.
        """
        stats = self.capture.build_stats()
        for value in DEFAULT_DATA_ERROR_lIMITS:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.between(0, value)
            self.assertEqual(
                f"The values must be between: {DEFAULT_LIMITS}",
                str(except_info.exception)
            )

    def test_between_values_validation_type_validation_error(self):
        """
        Test raise error in case of wrong type.
        """

        stats = self.capture.build_stats()
        for type_, value in DEFAULT_DATA_ERROR_TYPES:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.between(0, value)
            self.assertEqual(
                f"Only integer is allowed. Found: {type_}",
                str(except_info.exception)
            )

        for type_, value in DEFAULT_DATA_ERROR_TYPES:
            with self.assertRaises(DataCaptureValueError) as except_info:
                stats.between(value, 0)
            self.assertEqual(
                f"Only integer is allowed. Found: {type_}",
                str(except_info.exception)
            )
