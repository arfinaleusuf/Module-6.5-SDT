"""
Encapsulation হলো OOP-এর একটি concept যেখানে data (variables) এবং methods (functions) একসাথে একটি class-এর ভিতরে রাখা হয়, এবং বাইরের access control করা হয়।
"""

class BankAccount:
    def __init__(self, name, type,balance):
        self.name = name           # public variable
        self._type = type          # protected variable
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)

print(acc.get_balance())   # ✅ allowed
# print(acc.__balance)     # ❌ error (direct access not allowed)