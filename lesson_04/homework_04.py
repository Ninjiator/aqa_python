adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
print(f"Task 1 :\n{adventures_of_tom_sawer} \n")

# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
print(f"Task 2 :\n{adventures_of_tom_sawer} \n")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("  ", "")
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("   ", "")
print(f"Task 3 :\n{adventures_of_tom_sawer} \n")

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_counter = 0
for letter in adventures_of_tom_sawer:
    if letter == "h":
        h_counter = h_counter + 1
print(f"Task 4: \nLetter 'h' appears in text {h_counter} time's \n")
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
counter_capital = 0
for letter in adventures_of_tom_sawer:
    if letter.isupper():
        counter_capital = counter_capital + 1
print(f"Task 5 : \n{counter_capital} words starts with uppercase \n")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_entry = adventures_of_tom_sawer.find('Tom')
second_entry = adventures_of_tom_sawer.find('Tom', first_entry + 1)

print(f"Task 6 : \n Word Tom can be found 2th time by index = {second_entry} \n")
# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.strip(".").split(".") # strip(".") to delete last empty sentence
print(f"Task 7 : \n adventures_of_tom_sawer_sentences = {adventures_of_tom_sawer_sentences} \n")

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentences = adventures_of_tom_sawer_sentences[3]
print(f"Task 8 : \n fourth_sentences = {fourth_sentences} \n")

fourth_sentences_lower = adventures_of_tom_sawer_sentences[3].lower()
print(fourth_sentences_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("\nTask 9 :")
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.strip(" ").startswith("By the time"):
        print(sentence)

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
sentences_number = len(adventures_of_tom_sawer_sentences)
print(f"Task 10 : \n Number of sentences in adventures_of_tom_sawer_sentences is {sentences_number}")

sentence_split_by_words = adventures_of_tom_sawer_sentences[sentences_number-1].strip(" ").split(" ")
print("last sentence: ", sentence_split_by_words)

words_in_split_sentence = len(sentence_split_by_words)
print(words_in_split_sentence)
