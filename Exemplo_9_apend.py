# Autor:Bruno Manoel
# Data: 17/06/2024
# Versão: 1.0
# Algorítimo: Carros Utilizando o Apend. 
#  Descrição: 
# ====================================================

carros = ['W']

carros.append('GM') # Adiciona na ultima posição o Valor inserido
carros.append('FORD')
carros.append('FIAT')
carros.append('RENAULT')

print(carros)

carros.remove('FORD') # Remove através do nome do campo
print(carros)

carros.pop(3) # Remove através da posição do ao invez do nome do campo
print(carros)

print(len(carros))
carros.pop(len(carros)-1)

print(carros)




