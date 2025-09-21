# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

alice_in_wonderland = """ "Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don\'t much care where ——" said Alice.
"Then it doesn\'t matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough." """

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було\
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
sum_black_and_azov_sea = black_sea_area + azov_sea_area
print("\nSum of Black and Azov sea areas is : ", sum_black_and_azov_sea)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
products = 375291
products_from_storage_1_and_2 = 250449
storage_3 = products - products_from_storage_1_and_2
products_from_storage_2_and_3 = 222950
storage_1 = products - products_from_storage_2_and_3
storage_2 = products - storage_1 - storage_3
print("Products in storage 1 : ", storage_1)
print("Products in storage 2 : ", storage_2)
print("Products in storage 3 : ", storage_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
num_of_payments = 12 * 1.5
payment_amount = 1179
pc_price = payment_amount * num_of_payments
print("PC price is : ", pc_price)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
print("8019 % 8 = ", a)

b = 9907 % 9
print("9907 & 9 = ", b)

c = 2789 % 5
print("2789 % 5 = ", c)

d = 7248 % 6
print("7248 % 6 = ", d)

e = 7128 % 5
print("7128 % 5 = ", e)

f = 19224 % 9
print("19224 % 9 = ", f)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
large_pizza_amount = 4
large_pizza_price = 247

medium_pizza_amount = 2
medium_pizza_price = 218

juice_amount = 4
juice_price = 35

cake_amount = 1
cake_price = 350

water_amount = 3
water_price = 21

b_day_sum = large_pizza_amount*large_pizza_price + medium_pizza_amount*medium_pizza_price + juice_amount*juice_amount + cake_amount*cake_amount + water_price*water_price
print ("Cost of Iryna b-day is : ", b_day_sum)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photo_amount = 232
pictures_per_page = 8
pages_needed = photo_amount // pictures_per_page
print(f"Ihor needs {pages_needed} pages")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_range = 1600
fuel_usage = 9
tank_size = 48
amount_of_fuel_for_trip = 1600 / 100 * fuel_usage
gas_station_stops = int(amount_of_fuel_for_trip // tank_size)
print(f"For trip from Kharkiv to Budapest family needed = {amount_of_fuel_for_trip} liters of fuel")
print(f"Number of gas station stops is equal to {gas_station_stops}")
