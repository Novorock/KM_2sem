# Дано натуральное число. Найти количество нулей среди цифр числа
import sys

num = int(sys.argv[1])

counter = 0;

while num > 0:
    if (num%10) == 0:
        counter = counter + 1
    num = num // 10

print("Number of zeroes: " + str(counter))