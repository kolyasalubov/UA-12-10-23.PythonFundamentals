a = int(input("Enter your number:"))

produkt = 1 # число 1 вибрано через те що множення на 1 буде незмінним
while a > 0:
    digit =  a % 10 # Ділимо % на 10 з остачею кожне наступну цифру з числа а = 4285/10 = 5 (воно зберігається у змінній digit)
    produkt *= digit # Кожне число остачі перемножуємо на 1 щоб додати до добутку
    a //= 10 # число a оновлюється = 4285 ділимо //(без остачі,округлення до цілого) на 10 = 428
             # і так натупні числа в циклі доки а не стане 0
print(produkt)

a = int(input("Enter your number for reverse:"))
print(a % 10, end="")
print(a // 10 % 10, end="")
print(a // 100 % 10, end="")
print(a // 1000)

a = int(input("Enter your number:"))