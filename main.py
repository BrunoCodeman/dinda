import sys
from operations import Operations
from file_manipulation import get_accounts, generate_output_file

def get_things_done(accounts_file, transactions_file):
    op = Operations(accounts_file)
    transactions = get_accounts(transactions_file)
    for account_id, amount in transactions.items():
        op.make_operation(account_id, amount)
    generate_output_file(op.accounts)


if __name__ == '__main__':
    try:
        get_things_done(sys.argv[1], sys.argv[2])
    except Exception, e:
        raise