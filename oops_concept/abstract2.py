from abc import ABC, abstractmethod


# ============================================
# Example 1: Basic Abstract Class
# ============================================
class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses"""
        pass

    def describe(self):
        """Concrete method - can be used by all subclasses"""
        return f"This is a {self.__class__.__name__}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# ============================================
# Example 2: Abstract Class with Properties
# ============================================
class Vehicle(ABC):
    """Abstract vehicle class"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @property
    @abstractmethod
    def fuel_type(self):
        """Abstract property"""
        pass


class Car(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self._fuel_type = fuel

    def start_engine(self):
        return f"{self.brand} {self.model} engine started"

    def stop_engine(self):
        return f"{self.brand} {self.model} engine stopped"

    @property
    def fuel_type(self):
        return self._fuel_type


# ============================================
# Example 3: Payment Processing System
# ============================================
class PaymentProcessor(ABC):
    """Abstract payment processor"""

    @abstractmethod
    def validate_payment(self, amount):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass


class CreditCardProcessor(PaymentProcessor):
    def validate_payment(self, amount):
        if amount <= 0:
            return False
        return True

    def process_payment(self, amount):
        if self.validate_payment(amount):
            return f"Processing ${amount} via Credit Card"
        return "Invalid payment amount"

    def refund(self, transaction_id):
        return f"Refunding transaction {transaction_id}"


class PayPalProcessor(PaymentProcessor):
    def validate_payment(self, amount):
        if amount <= 0 or amount > 10000:
            return False
        return True

    def process_payment(self, amount):
        if self.validate_payment(amount):
            return f"Processing ${amount} via PayPal"
        return "Invalid payment amount"

    def refund(self, transaction_id):
        return f"PayPal refund for {transaction_id}"


# ============================================
# Example 4: Database Connection Interface
# ============================================
class Database(ABC):
    """Abstract database interface"""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass


class MySQLDatabase(Database):
    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connected = False

    def connect(self):
        self.connected = True
        return f"Connected to MySQL: {self.database} at {self.host}"

    def disconnect(self):
        self.connected = False
        return "Disconnected from MySQL"

    def execute_query(self, query):
        if not self.connected:
            return "Not connected to database"
        return f"Executing MySQL query: {query}"


# ============================================
# TESTING THE EXAMPLES
# ============================================
if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Shapes")
    print("=" * 50)

    # This would raise an error: shape = Shape()
    rect = Rectangle(5, 3)
    circle = Circle(4)

    print(rect.describe())
    print(f"Rectangle area: {rect.area()}")
    print(f"Rectangle perimeter: {rect.perimeter()}")
    print(f"\nCircle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")

    print("\n" + "=" * 50)
    print("Example 2: Vehicles")
    print("=" * 50)

    car = Car("Toyota", "Camry", "Gasoline")
    print(car.start_engine())
    print(f"Fuel type: {car.fuel_type}")
    print(car.stop_engine())

    print("\n" + "=" * 50)
    print("Example 3: Payment Processing")
    print("=" * 50)

    cc = CreditCardProcessor()
    paypal = PayPalProcessor()

    print(cc.process_payment(100))
    print(paypal.process_payment(500))
    print(cc.refund("TXN12345"))

    print("\n" + "=" * 50)
    print("Example 4: Database")
    print("=" * 50)

    db = MySQLDatabase("localhost", "myapp")
    print(db.connect())
    print(db.execute_query("SELECT * FROM users"))
    print(db.disconnect())