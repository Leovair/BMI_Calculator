# BMI calculator software
from colorama import init, Back, Style

init()

print(Back.GREEN + "Hello, welcome to BMI calculator!")

# input data
while True:
    print(Back.CYAN)
    try:
        weight = float(input("What is you weight?: "))
    except ValueError:
        print("Введено не число")
        continue
    print(Back.WHITE)
    try:
        height = float(input("And what is you height in cm?: "))
    except ValueError:
        print("Введено не число")
        continue
    print(type(weight))

    bmi = float(weight / (height / 100) ** 2)
    print(Back.RESET + "You current BMI is: " + f"{bmi:.2f}")
    if (bmi <= 16):
        print(Back.RED + "High body mass deficit", end='')
    elif (bmi >= 16 and bmi <= 18.5):
        print(Back.YELLOW + "Insufficient body weight", end='')
    elif (bmi >= 18.5 and bmi <= 25):
        print(Back.GREEN + "You weight is ok", end='')
    elif (bmi >= 25 and bmi <= 30):
        print(Back.YELLOW + "Excess body weight", end='')
    elif (bmi >= 30 and bmi <= 35):
        print(Back.RED + "Obesity of the 1 degree", end='')
    elif (bmi >= 35 and bmi <= 40):
        print(Back.RED + "Obesity of the 2 degree", end='')
    elif (bmi > 40):
        print(Back.RED + "Obesity of the 3 degree(morbid)", end='')


    print(Back.WHITE)
    quit_from_programm = input('\n[Q]quit or [A]gain ')
    if quit_from_programm == 'q':
        break
    elif quit_from_programm == 'a':
        continue

print(Style.RESET_ALL)
