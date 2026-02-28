import math

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
num3 = int(input("Informe o terceiro valor: "))

print ( bool (num3 >= 0 and num3 <= 10))
print ( bool (num1 < 0 or num1 >10)) #solucao 1
print ( bool (not(num1 > 0 or num1 <= 10))) #solucao 2
print ( bool (num2 > num1 and num2 > num3))
print ( bool (num2 % 7 == 0))
print(bool(num2 % num3 == 0 or num2 % num3 == 0))
# print ( bool (math.gcd(num2,num3)))
print ( bool (num1 == num2 and num1 == num3))
print ( bool (num1 == num2 or num1 == num3 or num2 == num3))