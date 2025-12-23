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


