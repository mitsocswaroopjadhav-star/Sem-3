from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class Card(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")

class NetBanking(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Net Banking")


class PaymentProcessor:
    def set_payment(self, payment):
        self.payment = payment

    def process(self, amount):
        self.payment.pay(amount)

processor = PaymentProcessor()

print("1. UPI")
print("2. Card")
print("3. Net Banking")

choice = int(input("Enter choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    processor.set_payment(UPI())
elif choice == 2:
    processor.set_payment(Card())
elif choice == 3:
    processor.set_payment(NetBanking())
else:
    print("Invalid Choice")
    exit()

processor.process(amount)



# #Output
# 1. UPI
# 2. Card
# 3. Net Banking
# Enter choice: 1
# Enter amount: 1000
# Paid 1000 using UPI
