print('Input any number of symbols: ')
user_input = input()

uniq_symbols_from_user_input = set(user_input)
if len(uniq_symbols_from_user_input) >= 10:
    print('True')
else:
    print('False')

