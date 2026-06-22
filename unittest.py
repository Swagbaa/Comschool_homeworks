import unittest

#N1 ---------------------------------------
# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def sub(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError
#         return a / b
#
# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         self.calc = Calculator()
#
#     def test_add(self):
#         self.assertEqual(self.calc.add(5, 3), 8)
#
#     def test_subtract(self):
#         self.assertEqual(self.calc.sub(10, 4), 6)
#
#     def test_multiply(self):
#         self.assertEqual(self.calc.multiply(6, 7), 42)
#
#     def test_divide(self):
#         self.assertEqual(self.calc.divide(20, 4), 5)
#
#     def test_divide_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             self.calc.divide(10, 0)
#
# if __name__ == '__main__':
#     unittest.main()

#N2 ----------------------------------------------------------

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError(f'Amount {amount} exceeds balance')
#         self.balance -= amount
#
#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError(f'Amount {amount} must be positive')
#         self.balance += amount
#
# class TestBankAccount(unittest.TestCase):
#     def setUp(self):
#         self.bank = BankAccount(100)
#
#     def test_balance(self):
#         self.account.deposit(100)
#         self.account.withdraw(30)
#         self.assertEqual(self.account.balance, 170)
#
#     def test_negative(self):
#         with self.assertRaises(ValueError):
#             self.account.deposit(-100)
#
#     def test_withdraw(self):
#         with self.assertRaises(ValueError):
#             self.account.withdraw(300)
#
# if __name__ == '__main__':
#     unittest.main()

#N3 -----------------------------------------

def get_status(response):
    if "status" not in response:
        raise KeyError("status not found")
    return response["status"]

class TestGetStatus(unittest.TestCase):

    def test_status_exists(self):
        data = {
            "status": "success",
            "message": "Operation completed"
        }
        self.assertEqual(get_status(data), "success")

    def test_status_not_exists(self):
        data = {
            "message": "Operation completed"
        }
        with self.assertRaises(KeyError):
            get_status(data)

    def test_status_number(self):
        data = {
            "status": 200
        }
        self.assertEqual(get_status(data), 200)


if __name__ == "__main__":
    unittest.main()