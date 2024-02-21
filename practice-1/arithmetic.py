answer = 4 * 100 - 54
equation = "4 * 100 - 54"
input_answer = input(f"Обчисліть приклад: {equation}\n")

if answer == int(input_answer):
    print("Правильно")
else:
    print(f"Неправильно. Правильна відповідь: {answer}")