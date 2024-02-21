num1 = 7
num2 = 12

res_and_1 = (num1 < num2) and (num1 + num2 > 10)
res_and_2 = (num1 * 2 == num2) and (num2 % 2 == 0)

print(f"Результат 1 з оператором and: {res_and_1}") # true
print(f"Результат 2 з оператором and: {res_and_2}") # false

res_or_1 = (num1 < num2) or (num1 + num2 > 20)
res_or_2 = (num1 * 3 == num2) or (num2 % 5 == 0)

print(f"Результат 1 з оператором or: {res_or_1}") # true
print(f"Результат 2 з оператором or: {res_or_2}") # true

str1 = "hello"
str2 = "world"
res_str_and = (len(str1) > 3) and (str2.isnumeric())  # false
res_str_or = (len(str1) > 3) or (str2.isnumeric())  # true

print(f"Результат зі str типом та and: {res_str_and}")
print(f"Результат зі str типом та or: {res_str_or}")

user_num1 = float(input("Введіть перше число: "))
user_num2 = float(input("Введіть друге число: "))

comparison = user_num1 > user_num2
print(f"Результат порівняння двох введених чисел: {comparison}")
