# Autor: Bruno Manoel
# Data: 06/06/2024
# Versão: 1.0
# Objetivo: Exercício 8 - Multa Velocidade  
# Descrição   : Escreva um programa que leia a velocidade máxima em uma avenida e velocidade com que o motorista
#                               Estava dirigindo nela e calclule a multa que uma pessoa vai receber.        
#                        
#                        Valocidade            Classificação
#                        Até 10 Km/h                R$ 50,00
#                        De 11 a 30 Km/h           R$ 100,00
#                        mais que 31 Km/h          R$ 200,00
#                        
#===========================================================
# Variáveis

limite_velocidade = 0
velocidade_motorista = 0
dif_velocidade = 0
velocidade = 0
classificacao = ''
#entrada

# velocidade=float(input('insira a velocidade do veículo:'))

limite_velocidade = int(input('insira a velocidade da via'))
velocidade_motorista = int(input('insira a velocidade da pista'))

# processamento

dif_velocidade=velocidade_motorista-limite_velocidade

#processamento


if(dif_velocidade >0 and dif_velocidade <= 10):
    classificacao = 'sua multa será de 50,00'

elif(dif_velocidade >= 11 and dif_velocidade <= 30):
    classificacao = 'sua multa será de R$ 100,00'

elif(dif_velocidade >= 31):
    classificacao = 'sua multa será de R$ 200,00'

else:
    classificacao = 'R$0,001'

#saída
print (classificacao)

#===========================================================


