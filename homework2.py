first = 6
second = 16
third = 65

age = input("Ведіть свій вік : ")
age = int(age)

if age < first :
    print("Де твої батьки?")
elif age < second :
    print("Це фільм для дорослих!")
elif age > third :
    print("Покажіть пенсійне посвідчення!")
elif "7" in str(age) :
    print("Вам пощастить!")
else :
    print("А білетів вже немає!")
