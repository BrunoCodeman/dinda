from random import randint


def create_files():
    accounts_file = open('accounts.csv', 'w')
    transactions_file = open('transactions.csv', 'w')

    for i in range(1, 1000, 1):
        account_id = randint(1, 1000)
        accounts_file.write('%i, %i \n' %
                            (account_id, randint(-99999999, 99999999)))
        transactions_file.write('%i, %i \n' % (
            account_id, randint(-99999999, 99999999)))

    accounts_file.close()
    transactions_file.close()
