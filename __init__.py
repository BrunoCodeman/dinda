def get_accounts(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        accounts = []

        for line in lines:
            data = line.split(', ')
            accounts.append({"id": data[0], "amount": long(data[1])})

        return accounts
    except Exception:
        raise

def generate_output_file(accounts):
    f = open('accounts_after_transaction.csv', 'w')
    for account in accounts:
        f.write('%s, %i \n' % (account['id'], account['amount']))
    f.close()