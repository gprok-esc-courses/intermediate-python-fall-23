
accounts_file = open('accounts.csv')

lines = accounts_file.readlines()

for line in lines:
    tokens = line.split(',')
    print(tokens)
    print(tokens[1])
