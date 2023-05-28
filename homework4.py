# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
def count_words_with_two_vowels_in_sentence(text):
    vowels = "a, e, i, o, u, y, я, ю, ї, и, ы, у, о, е, а, і"
    words_list = text.split()
    count = 0
    for words in words_list:
        for i in range(len(words) - 1):
            if words[i] in vowels and words[i+1] in vowels:
                count += 1
                break
    return count

input_string = input("Введіть рядок: ")
result = count_words_with_two_vowels_in_sentence(input_string)
print("Кількість слів з двома голосними літерами підряд:", result)

#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
price = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

min_prices = 37.166
max_prices = 49.999

for shop, price in price.items():
    if min_prices < price < max_prices:
        print(shop)