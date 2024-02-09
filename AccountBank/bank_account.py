class BankAccount:
    def __init__(self):
        self.money = 0
        self.status = ''

    def get_balance(self):
        if self.status == 'open':
            return self.money
        else:
            raise ValueError('account not open')

    def open(self):
        if self.status == '':
            self.status = 'open'
        else:
            raise ValueError('account already open')

    def deposit(self, amount):
        if self.status == 'open':
            if amount >= 0:
                self.money += amount
            else:
                raise ValueError('amount must be greater than 0')
        else:
            raise ValueError('account not open')

    def withdraw(self, amount):
        if self.status == 'open':
            if self.money >= amount:
                if amount >= 0:
                    self.money -= amount
                else:
                    raise ValueError("amount must be greater than 0")
            else:
                raise ValueError('amount must be less than balance')
        else:
            raise ValueError('account not open')

    def close(self):
        if self.status == 'open':
            self.status = ''
            self.money = 0
        else:
            raise ValueError('account not open')

