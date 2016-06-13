# coding: utf-8
from .. import get_accounts, generate_output_file

class Operations(object):
    """class to manipulate accounts"""

    def __init__(self, file_name):
        self.accounts = get_accounts(file_name)

    def make_operation(account, value):
        return self.debit_operation(account, value) if value < 0 else self.credit_operation(account, value)

    def debit_operation(account, value):
        # se a conta estiver negativa, tira mais 5 pilas
        pass

    def credit_operation(account, value):
        pass

    def get_account_by_id(account_id):
        get_account = lambda x: x['id'] == account_id
        return filter(get_account, self.accounts)


