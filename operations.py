# coding: utf-8
import math
from file_manipulation import get_accounts, generate_output_file

class Operations(object):
    """class to manipulate accounts"""

    def __init__(self, file_name):
        self.accounts = get_accounts(file_name)

    def make_operation(self, account_id, value):
        return self.debit_operation(account_id, value) if value < 0 else self.credit_operation(account_id, value)

    def debit_operation(self, account_id, value):
        # se a conta estiver negativa, tira mais 5 pilas
        tax = 500
        account = self.accounts[account_id]
        new_amount = long(account - math.fabs(value))
        self.accounts[account_id] = new_amount if new_amount > 0 else long(new_amount - tax)
        

    def credit_operation(self, account_id, value):
        self.accounts[account_id] += long(math.fabs(value))

