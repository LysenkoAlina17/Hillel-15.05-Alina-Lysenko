
#Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".

word = input("Ведіть слово : ")
index = input("Ведіть номер символу : ")
index = int(index)
symbol = word [index - 1]
print (f'The {index} symbol in {word}" is "{symbol}"')

#Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних
my_str = input("Ведіть речення : ")
word = my_str.split()
word = len(word)
print(word)

#Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
list1 = ['1', '2', 3 , True, 'False', 5, '6', 7 , 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = [element for element in list1 if isinstance(element, (int, float)) and not isinstance(element, bool)]
print(list2)

#або
list3 = ['1', '2', 3 , True, 'False', 5, '6', 7 , 8, 'Python', 9, 0, 'Lorem Ipsum']
list4 = []
for element in list3:
    if isinstance(element, (int,float)) and not isinstance(element, bool):
        list4.append(element)
print(list4)
