def get_accounts(file_name):
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        accounts = {}

        for line in lines:
            data = line.split(', ')
            accounts[data[0]] = long(data[1])
            #accounts.append({ data[0], "amount": long(data[1])})
        return accounts
    except Exception:
        raise

def generate_output_file(accounts):
    f = open('accounts_after_transaction.csv', 'w')
    for account_id, amount in accounts.items():
        f.write('%s, %i \n' % (account_id, amount))
    f.close()