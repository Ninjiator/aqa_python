while True:
    print('Input word with letter h or H')
    user_input = input()
    if user_input.find('h') != -1 or user_input.find('H') != -1:
        print('Letter h or H is here')
        break
