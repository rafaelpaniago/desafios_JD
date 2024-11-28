# IS INSTANCE
# Ele vai checar. Avalia pra mim se determinada coisa é um inteiro.

numero = int(input('Digite um número: '))
if isinstance(numero, int):
    print('É um inteiro')
else:
    print('Não é um inteiro')