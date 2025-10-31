"""
# 🧩 Unit Testing in Python — Overview

## 📘 Introduction
**Unit testing** is the process of testing **individual units or components** of a program in isolation  
to ensure that each part works as intended.  

A *unit* is the smallest testable piece of code — usually a **function, method, or class**.  
Unit tests help detect bugs early, simplify debugging, and make code more reliable and maintainable.

---

### 3. Links
[Unit test - Corey Schafer](https://www.youtube.com/watch?v=6tNS--WetLI)
[Unit test apis](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug)


## 🧪 Common Assertion Methods

| **Method** | **Checks That** | **New in (Python)** |
|-------------|----------------|---------------------|
| `assertEqual(a, b)` | `a == b` | — |
| `assertNotEqual(a, b)` | `a != b` | — |
| `assertTrue(x)` | `bool(x) is True` | — |
| `assertFalse(x)` | `bool(x) is False` | — |
| `assertIs(a, b)` | `a is b` | 3.1 |
| `assertIsNot(a, b)` | `a is not b` | 3.1 |
| `assertIsNone(x)` | `x is None` | 3.1 |
| `assertIsNotNone(x)` | `x is not None` | 3.1 |
| `assertIn(a, b)` | `a in b` | 3.1 |
| `assertNotIn(a, b)` | `a not in b` | 3.1 |
| `assertIsInstance(a, b)` | `isinstance(a, b)` | 3.2 |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` | 3.2 |
| `assertIsSubclass(a, b)` | `issubclass(a, b)` | 3.14 |
| `assertNotIsSubclass(a, b)` | `not issubclass(a, b)` | 3.14 |


## 🎯 Purpose
- Verify that each **function or class performs correctly**.  
- Detect issues early during development.  
- Facilitate **refactoring** and continuous integration.  
- Serve as **documentation** for expected behavior.  

---

## ⚙️ Key Concepts
- **Test Case:** A single unit test that checks a specific behavior.
- **Test Suite:** A collection of related test cases.
- **Assertions:** Statements used to verify that the expected output matches the actual result.
- **Mocking:** Simulating external dependencies or objects to isolate code under test.

---

## 🧪 Example (Using unittest)
```python
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

if __name__ == "__main__":
    unittest.main()


How to run the unit test
python -m unittest unit_testing.py
"""

from unittest.mock import patch
import unittest
import requests


#=============================================================================
#🧩 Unit Testing
#=============================================================================

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
        

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertRaises(ValueError,divide,10,0)

        #With context manager
        with self.assertRaises(ValueError):
             divide(10, 0)

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
    unittest.main()