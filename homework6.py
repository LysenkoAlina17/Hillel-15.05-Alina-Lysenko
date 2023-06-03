#Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.
def to_float (value):
    try :
        float_value = float(value)
        return float_value
    except (ValueError, TypeError):
        return 0.0

value1 = to_float (5)
print(value1)

value2 = to_float("3,14")
print(value2)

value3 = to_float("beagle")
print(value3)

value4 = to_float([1, 2, 3])
print(value4)

#Напишіть функцію, що приймає два аргументи. Функція повинна
#якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
#у будь-якому іншому випадку повернути кортеж з цих аргументів

def process_argument (arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return (arg1, arg2)

res1 = process_argument (3,5)
print(res1)

res2 = process_argument (6.5, 5.7)
print(res2)

res3 = process_argument ("Beagle",  "puppy")
print(res3)

res4 = process_argument ("Beagle", 5.5)
print(res4)

#Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#Попросіть користувача ввести свсвій вік.
#- якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
#- якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
#- якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
#- якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
#- у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад :

def get_year_form(age):
    if age == 1:
        return "рік"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "роки"
    else:
        return "років"
def get_tiket_price (age):
    if age < 7:
        return(f"Тобі ж {age} {get_year_form(age)}! Де твої батьки?")
    elif age < 16:
        return(f"Тобі лише {age} {get_year_form(age)}, а це е фільм для дорослих!")
    elif age > 65:
        return(f"Вам {age} {get_year_form(age)}? Покажіть пенсійне посвідчення!")
    elif "7" in str(age):
        return(f"Вам {age} {get_year_form(age)}, вам пощастить")
    else:
        return(f"Незважаючи на те, що вам {age} {get_year_form(age)}, білетів всеодно нема!")

user_age = int(input("Введіть свій вік:"))
res = get_tiket_price(user_age)
print(res)
