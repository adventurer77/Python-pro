from abc import ABC, abstractmethod

@abstractmethod
class PaymentInstrument(ABC):
    def make_payment(self, amount: float):
        pass


class CreditCard(PaymentInstrument):

    def __init__(self, number: str, expiration_date: str, cvv: str):
        self.number = number
        self.expiration_date = expiration_date
        self.cvv = cvv
       
    
    def make_payment(self, amount: float):
        print(f"Making a payment from credit card {self.number} for the amount {amount}")
        return True
        

class BankTransfer(PaymentInstrument):

    def __init__(self, sender_account: str, recipient_account: str):
        self.sender_account = sender_account
        self.recipient_account = recipient_account

    def make_payment(self, amount: float) -> bool:
        
        print(f"Making a bank transfer from account {self.sender_account} to account {self.recipient_account} for the amount {amount}")
        return True

class EWallet(PaymentInstrument):

    def __init__(self, number: str, balance: float):
        self.number = number
        self.balance = balance

    def make_payment(self, amount: float) -> bool:
        
        if self.balance >= amount:
            self.balance -= amount
            print(f"Making a payment from e-wallet {self.number} for the amount {amount}")
            return True
        else:
            print(f"Insufficient funds on e-wallet {self.number}")
            return False
        
        


class PaymentProcessor:

    def __init__ (self):
        self.payment_instruments = []

    def add_payment_instrument(self,payment_instrument:PaymentInstrument):
        self.payment_instruments.append(payment_instrument)

    def make_payment(self,payment_instrument:PaymentInstrument,amount:float):
        if payment_instrument not in self.payment_instruments:
            print(f"Payment instrument {payment_instrument} not found.")

        return payment_instrument.make_payment(amount)



credit_card = CreditCard("1234-5678-9012-3456", "12/24", "123")
bank_transfer = BankTransfer("UA12345678901234567890", "UA98765432109876543210")
e_wallet = EWallet("EW1234567890", 1000.0)

# Create payment processor
payment_processor = PaymentProcessor()

# Add payment instruments to processor
payment_processor.add_payment_instrument(credit_card)
payment_processor.add_payment_instrument(bank_transfer)
payment_processor.add_payment_instrument(e_wallet)


payment_processor.make_payment(credit_card, 500.0)
payment_processor.make_payment(bank_transfer, 100.0)
payment_processor.make_payment(e_wallet, 200.0)