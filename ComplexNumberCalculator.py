# Для запуска приложения вам нужно запустить файл 
# calculator.py в вашей среде разработки 
# или из командной строки с помощью команды 
# python calculator.py.


class ComplexNumberCalculator:
    def add(self, num1, num2):
        real_part = num1[0] + num2[0]
        imag_part = num1[1] + num2[1]
        return (real_part, imag_part)

    def multiply(self, num1, num2):
        real_part = num1[0]*num2[0] - num1[1]*num2[1]
        imag_part = num1[0]*num2[1] + num1[1]*num2[0]
        return (real_part, imag_part)

    def divide(self, num1, num2):
        den = num2[0]**2 + num2[1]**2
        real_part = (num1[0]*num2[0] + num1[1]*num2[1]) / den
        imag_part = (num1[1]*num2[0] - num1[0]*num2[1]) / den
        return (real_part, imag_part)

calculator = ComplexNumberCalculator()

# Пример использования
num1 = (1, 2)
num2 = (3, 4)

result_add = calculator.add(num1, num2)
result_multiply = calculator.multiply(num1, num2)
result_divide = calculator.divide(num1, num2)

print("Addition result:", result_add)
print("Multiplication result:", result_multiply)
print("Division result:", result_divide)

