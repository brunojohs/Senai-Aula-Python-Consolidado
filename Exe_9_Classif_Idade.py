# Autor: Bruno Manoel
# Data: 04/06/2024
# Versão: 1.0
# Objetivo: Exercício 8 - Classificação de Idade  
# Descrição   : Escreva um programa que leia a idade de um indivpiduo e escreva a faixa etária que pertencae de acirdi cin a tabela abaixo:
#                        
#                        Faixa Etária       Classificação
#                            <=12                Criança
#                            13~17             Adolescente
#                            18~59              Adulto
#
#===========================================================

# Declaração de Variáveis:
idade = 0
classificacao = ''    

# entrada 

idade = int(input('insira a sua Idade:'))

# processamento

if(idade >= 0 and idade <= 12):
    classificacao = 'Criança'


elif(idade >= 13 and idade <= 17):
    classificacao = 'Adolescente'


elif(idade >= 17 and idade <= 59):
    classificacao = 'Adulto'

else:
    classificacao = 'Adulto Senior'
#saída
print (classificacao)

#==============================================================================
   