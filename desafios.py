# Escreva um programa que some dois números inseridos pelo usuário.

# num1 = int(input('Digite um número -> '))
# num2 = int(input('Digite outro número -> '))

# print(num1+num2)


# Escreva um programa que receba um número e calcule o resto da divisão desse úmero por 5

# num1 = int(input('Digite um número -> '))
# rest_5 = num1 % 5

# print(f'O resto da divisão do número {num1} por 5 é igual a: {rest_5}')





# Crie um programa que calculo a média de dois números flutuantes

# def media(a,b):
#     return (a+b)/2


# num1 = float(input('Digite o primeiro número: '))
# num2 = float(input('Digite o segundo número: '))

# print(f'A média dos números é: {media(num1,num2)}')



# Escreva um programa que concatene duas strings fornecidas pelo usuário

# string1 = input('Digite uma palavra: ')
# string2 = input('Digite outra palavra: ')

# print(string1, string2)




# Escreva um programa que receba uma data e separe o dia, mês e ano em uma lista

# data = input('Digite a data nesse formato DD/MM/AAAA -> ')
# data_split = data.split('/')

# print(f'O dia é {data_split[0]}. O mês é {data_split[1]}. O ano é {data_split[2]}.')



# Escreva um programa usando try except
# Try except é usado para tratar erros.

def divisao(a,b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Divisão por zero."
    return resultado

print(divisao(9,3))
print(divisao(2,0))

