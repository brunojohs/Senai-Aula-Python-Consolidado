# Auto: Bruno Manoel
# Data: 28/05/2024
# Versão: 1.0
# Objetivo: Exercício 6 elif 
# Descrição:       Excreva um algorítimo para exibir o nome do lanche de acordo com o número inserido pelo usuário de acordo com a tabela abaixo:
#
#               ------------------------------------
#               Exemplo de Execução:    
#                   Nr.     Lanche
#                   1       Big Mac   
#                   2       Quarteirão
#                   3       Mc Chicken
#                   4       Chedar Mc Melt
#                   5       Mc Fish 
#               ------------------------------------               
#             
#===========================================================
# Declaração de Variáveis:
nr = 0 
lanche_escolhido = '' 

# entrada 

print (' Nr. do lanche \n 1. BigMac \n 2. Quarteirão \n 3. Mc Chiken \n 4. Chedar Mc Melt \n 5. Mc fish')
nr = int(input('insira o número do Lanche de 1 a 5:'))

# processamento
if (nr == 1):
    lanche_escolhido ='Big mac'

elif (nr == 2):
    lanche_escolhido = 'Quarteirão'

elif (nr == 3):
    lanche_escolhido = 'Mc Chiken'

elif (nr == 4):
    lanche_escolhido = 'Chedar Mc Melt'

elif (nr == 5):
    lanche_escolhido = 'Mc Fish'

else:   
    lanche_escolhido ('Opção inválida, Digite um número de acordo com a instrução de 1 a 5')

print(lanche_escolhido)

#==============================================================================
   



