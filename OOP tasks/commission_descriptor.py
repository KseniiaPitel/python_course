class Value:
    def __init__(self):
        self.amount = None
        #super().__init__(commision)


    @staticmethod
    def _calculated_value(amount):
        return amount * 11

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, amount):
        self.amount = self._calculated_value(amount)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.2)
new_account.amount = 100

print(new_account.commission)
print(new_account.amount)

print(issubclass(Value, Account))
