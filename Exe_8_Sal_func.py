# Autor: Bruno Manoel
# Data: 04/06/2024
# Versão: 1.0
# Objetivo: Exercício 8 - Aumento de Salário  
# Descrição   : Faça um programa que recebe o salário de um funcionário, calcule e mostre o novo salário, sabendo que:
#                        
#                        1 Salário < R$ 1000,00 aumento de 25%
#                        2 Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%
#                        3 Salário >= R$ 2000,00 aumento de 10%
#
#===========================================================

# Declaração de Variáveis:
salario = 0 
salario_aumento = 0

# entrada 

salario=float(input('insira o valor do salário, para que possamos calcular o seu merecido Aumento Salarial Você Mereceu' ))

# processamento

if(salario < 1000):
    salario_aumento = salario * 1.25
    print('Você terá um aumento de 25%')
    print('seu novo salario será', salario_aumento)
    
elif(salario >= 1000 and salario < 2000):
    salario_aumento = salario * 1.15
    print('Você terá um aumento de 15%')
    print('seu novo salario será', salario_aumento)

elif(salario >= 2000):
    salario_aumento = salario * 1.10
    print('Voce terá um aumento de 10%')
    print('seu novo salario será', salario_aumento)

salario_aumento = round (salario_aumento)
#==============================================================================
   

