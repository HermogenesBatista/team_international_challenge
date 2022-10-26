# Copyright (c) 2021 Intelligent Startup Consulting LLC.
# All rights reserved.
# This software is proprietary and confidential and may not under
# any circumstances be used, copied, or distributed.
import unittest

from data_capture import DataCapture


class TestDataCapture(unittest.TestCase):

    def test_less_values(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(2, stats.less(4))
        self.assertEqual(0, stats.less(3))
        self.assertEqual(3, stats.less(6))
        self.assertEqual(4, stats.less(9))
        self.assertEqual(5, stats.less(10))

    def test_greater_values(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(stats.greater(0), 5)
        self.assertEqual(stats.greater(2), 5)
        self.assertEqual(stats.greater(3), 3)
        self.assertEqual(stats.greater(4), 2)
        self.assertEqual(stats.greater(7), 1)
        self.assertEqual(stats.greater(8), 1)
        self.assertEqual(stats.greater(9), 0)
        self.assertEqual(stats.greater(10), 0)

    def test_between_values(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()
        self.assertEqual(4, stats.between(3, 6))
        self.assertEqual(2, stats.between(4, 6))
        self.assertEqual(3, stats.between(4, 9))
        self.assertEqual(1, stats.between(7, 12))
        self.assertEqual(5, stats.between(0, 9))
        self.assertEqual(5, stats.between(9, 0))
