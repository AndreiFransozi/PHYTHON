#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.#
F = int(input('Digite a temperatura em Fahrenheit{},: '))
C = 5 * ((F-32) / 9)
print('{}, em graus Fahrenheit. A temperatura em gruas celsius é igual a {}!'.format(F, C))
