lst1 = ['1', '2', '3', True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for k in lst1:
    if type(k) == str:
        lst2.append(k)

print('Here is a members of lst2 with type str')
for k in lst2:
    print(k)