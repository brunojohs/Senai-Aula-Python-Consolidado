# Autor:Bruno Manoel
# Data: 13/06/2024
# Versão: 1.0
# Algorítimo: Tabuada_2
# Descrição: Faça um programa que apresente a tabuada 1 ao 10: 
# ====================================================

print('Iniciando o programa #### tabuada Correção #### ')

repeticao = 0 # esta variável define de quanto a quanto a tabuada deve ser apresentada
indice = 0 # esta variavel faz a contagem de 0 a 10 para cada um dos calculos da tabuada Exemplo: 1x1 = 1 até o 1x10 = 10

for repeticao in range(11):
    for indice in range(11):
            print(f'{repeticao} x {indice} = {repeticao*indice}')

# ===================================================================

