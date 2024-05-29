def calcular(x, y, op =1):
    if(op == 1):
       print("a soma é :" ,x + y)
    elif(op == 2):
       print("O resto é :" ,x - y)
    elif(op == 3):
        print("produto é :" ,x * y)
    elif(op == 4):
       print("o quociente é: ",x / y)
    elif(op ==5):
       print(" o resto da divisão é:" ,x % y)
    elif(op == 6):
       print(' A potencia é:' ,x ** y)

x = int(input('digite um numero: '))
y = int(input('digite um numero: '))
print("OPERAÇÕES")
print("1 adição")
print("2 subtração")
print("3 multiplicação")
print("4 divisão")
print("5 resto da divisão")
print("6 potencia")
op =int(input('Escolhe a operação: '))
calcular(x, y, op)