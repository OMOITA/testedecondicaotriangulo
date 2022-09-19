print("Programa de identificação de triângulo")
print("-=-"*12)
num1 = float(input("Digite a primeiro lado: "))
num2 = float(input("Digite o segundo lado:  "))
num3 = float(input("Digite o terceiro lado: "))
#condição para existência de triângulos 
if abs(num2 -num3)<num1<num2+num3 and abs(num1 - num2)<num3<num1+num2 and abs(num1-num3)<num2<num1+num3:
    print("\033[1;32mÉ possível formar um triângulo\033[m")
else:
    print("\033[1;32mNão é possível formar um triângulo\033[m")
#condição dos triângulos
if num1==num2==num3 :
   print("\033[1;32mO Triângulo é equilatéro\033[m")
elif num1==num2<num3 or num2==num3<num1 or num3==num1<num2:
    print("\033[1;32mO Triângulo é isóscelels\033[m")
else:
    print("\033[1;32mO triângulo é Escaleno\033[m")