#define abstract class
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# define concreate one class
class CreditCard(Payment):
    def Validate_payment(self, amount):
        if amount < 0:
            return False
        return True

    def process_payment(self, amount):
        if self.Validate_payment(amount):
            return f"Processing {amount} via Credit Card"
        return "Invalid payment amount"



card=CreditCard()
print(card.process_payment(100))
print(card.process_payment(-100))

