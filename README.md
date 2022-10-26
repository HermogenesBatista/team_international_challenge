# Team International Code Challenge

## DataCapture analysis
In this simple application we want to calculate some statistical data from given set of numbers.
We need to implement a simple program that calculate how many occurrences per item, or how many items have lower/greater or between a given interval.

## Actions / Complexity

### build_stats
This action must be calculate all data that would be used in statistical actions linearity [O(n) complexity].

### add | less | greater | between
The time O(1) complexity expected, in other words solve it in constant time.

## How to run
You can run the tests:
```
python -m unittest test_data_capture.py
```

If you want to use in your code:
```python
from data_capture import DataCapture
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)  # expected return 2, because we had only 2 occurrences of value "3"
stats.greater(5)  # expected return 2, because we had 1 occurrences of values "6" and "9".
stats.between(0, 5)  # expected return 3, because we had 1 occurrences of value "3" and one to "4".
```
