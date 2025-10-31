""" Біометрична авторизація. 
   Функція виконує авторизацію на підставі отриманого списка словників даних та словника, отриманого з іншої функції від користувача.

    Параметри користувача: id - int, name - str, second_name - str, age - int
    Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ. 
    Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
    Функція повертає рівень доступу: full, read-only, forbiden """

import pytest

# варіант вхідних значень
database_users = [
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25},
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
]
# варіанти user_input :
users_input = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30},  # - full access
    {"id": 3, "name": "Max", "second_name": "Mad", "age": 55},
    {"id": 1, "name": "Mike", "second_name": "Mouse", "age": 15},
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25},  # - full access
    {"id": 200, "name": "Jane", "second_name": "Joi", "age": 25}  # another ID - read only
]


def biometrical_autorization(user_data):
    mismatch_count = 0
    mismatches = []
    for users in database_users:
        mismatch_count = 0
        if user_data["id"] != users["id"]:
            mismatch_count += 1
        if user_data["name"] != users["name"]:
            mismatch_count += 1
        if user_data["second_name"] != users["second_name"]:
            mismatch_count += 1
        if user_data["age"] != users["age"]:
            mismatch_count += 1
        mismatches.append(mismatch_count)

    result = min(mismatches)
    print(mismatches)
    print(result)
    match result:
        case 0:
            return "full-access"
        case 1:
            return "read-only"
        case _:
            return "forbiden"


print(biometrical_autorization(users_input[2]))


@pytest.mark.parametrize("user_input, expected", [
    (users_input[0], "full-access"),
    (users_input[1], "forbiden"),
    (users_input[2], "forbiden"),
    (users_input[3], "full-access"),
    (users_input[4], "read-only")
])
def test_biometrical_autorization(user_input, expected):
    assert biometrical_autorization(user_input) == expected