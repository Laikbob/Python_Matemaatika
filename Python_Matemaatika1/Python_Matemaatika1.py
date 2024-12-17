import random
print("Добро пожаловать на проверку знаний по математике .")
tase=input("Выберите сложносить ( Легко / Средне / Сложно ) :")

if tase == "Легко" :
    print(f"Вы выбрали {tase}")
    operations = ["+","-"]
    max_number = 15


elif tase == "Средне" :
    print(f"Вы выбрали {tase}")
    operations = ["+","-","*","/"]
    max_number = 30

elif tase == "Сложно" :
    print(f"Вы выбрали {tase}")
    operations = ["+","-","*","/","**"]
    max_number = 60

else:
    print("Неправильный выбор")
    exit()

correct_count = 0

for i in range(1, 6):
    num1=random.randint(1,max_number)
    num2=random.randint(1,max_number)
    operation=random.choice(operations)
    if operation == "+":
           correct_answer = num1 + num2
    elif operation == "-":
           correct_answer = num1 - num2
    elif operation == "*":
            correct_answer = num1 * num2
    elif operation == "/":
            correct_answer = num1 / num2
    elif operation == "**":
            correct_answer = num1 ** num2
            user_answer=float(input(f"{num1}{operation}{num2} = "))
    if user_answer == correct_answer:
        print("Правильно!")
        correct_count += 1
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")

percentage = (correct_count/ 5 ) * 100
if percentage < 60:
    grade = 2
elif percentage < 75:
    grade = 3
elif percentage < 90:
    grade = 4
else:
    grade = 5

print(f"Ваша оценка: {grade}")
