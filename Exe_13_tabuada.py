# Autor:Bruno Manoel
# Data: 13/06/2024
# Versão: 1.0
# Algorítimo: Tabuada
# Descrição: Faça um programa que calcule a tabuada de um numero digitado: 
# ====================================================

calculo = 0
indice = 0
resultado = 0

calculo = int(input('insira o número para o calculo: '))

for indice in range(11):
    resultado = calculo * indice
    print(f'{calculo} x {indice}={calculo*indice}')


#======



