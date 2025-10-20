import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    #Создаю цикл
 while True:
     try:
         guess = int(input("Ваш ответ: "))
         attempts += 1
         if guess < number:
             print("Слишком мало!")
         elif guess > number:
             print("Слишком много!")
         else:
             print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
             break
     except ValueError:
         print("Пожалуйста, введите число.")
guess_number()
