# Autor:Bruno Manoel
# Data: 13/06/2024
# Versão: 1.0
# Algorítimo: Prova
# Descrição: Faça um programa que receba dois valores, sendo que o primeiro deve ser menor que o segundo.
#            O programa dece apresentar tos os numeros impares contidos nesta sequencia. 
#             (Modulo %. Exemplo: 7%2 = 1)    
# ====================================================

# Variáveis

valores_1 = 0 # Indica o início do range
valores_2 = 0 # Indica o Final do range
resultado = '' # trata-se do intervalo a ser varrido
resto = 0 # o que sobre utilizando o Módulo (% 2) representa os números impares 

#entrada

valores_1 = int(input('insira o valor inicial do seu range : '))
valores_2 = int(input('insira o valor final do seu range : '))

# Processamento 

for resultado in range (valores_1, valores_2): # indica o range a ser varrido 
    resto = resultado % 2
    
    if resto == 1:
        print('sequencia de contagem dos números impares' , resultado)


# resultado = (valores_1 + valores_2) % 2
# print('o resultado é:' , resultado)

#==============================================================================================

#Processamento

#Saída

# ===================================================================