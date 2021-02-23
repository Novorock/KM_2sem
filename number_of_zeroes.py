# Дано натуральное число. Найти количество нулей среди цифр числа
import sys

try:
    num = int(sys.argv[1])

    if num > 0:
        counter = 0

        while num > 0:
            if num % 10 == 0:
                counter = counter + 1
            num = num // 10

        print("Number of zeroes: " + str(counter))
    else:
        print("Natural number is expected instead of: " + str(num))
except ValueError:
    print("Invalid input")
