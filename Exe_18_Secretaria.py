# Autor:Bruno Manoel
# Data: 17/06/2024
# Versão: 1.0
# Algorítimo: Secretaria 
#  Descrição:  Faça um programa que adicione ao sistena da escola (array) ou remova um aluno específico.
#               Nesse sistema deve etar previsto um menor contendo as 03 opções:
# ==============================================================================
#Sistema SENAI
#   1 - Adicionar aluno:
#   2 - Remover aluno:
#   3 - Apresentar alunos
#   4 - Sair
#  Insira a opção desejada: 
#===================================   
# Adicionar aluno
# Insira o nome do aluno:
#=================================   
#Remover aluno
#Insira o nome do aluno para ser removido:
#===================================   
#Alunos no sistema
#['João', 'Pedro','Luana']
#===================================   

alunos = 0 # numero inteiro
sistema_alunos = [] # Array
novo_aluno = '' # String vazia
delete_alunos = '' 

while True:

    print ('Bem Vindos ao Portal de Sistemas do Senai: Digite a opção desejada sendo:')
    print ('1 para Adicionar Aluno') 
    print ('2 para Remover Aluno') 
    print ('3 para Apresentar')   
    print ('4 Sair')

    alunos = int(input('insira o número da Opção:'))

    if (alunos ==1):
        opção_escolhida = '1 Adicionar Aluno' 
        print(opção_escolhida) 
        novo_aluno = input('Digite o nome do novo Aluno:')
        sistema_alunos.append(novo_aluno)

    elif (alunos == 2):
        opção_escolhida = '2 Remover Aluno' 
        print(opção_escolhida) 
        delete_aluno = input('Digite o nome do Aluno a ser Deletado:')
        sistema_alunos.remove(delete_aluno)

    elif (alunos == 3):
        opção_escolhida = '3 Apresentar Aluno' 
        print(opção_escolhida) 
        print(sistema_alunos)

    elif (alunos >= 5):
        opção_escolhida = '=> 5 Opção Inválida tente novamente' 
        print(opção_escolhida) 
       
    elif (alunos == 4):
        opção_escolhida = '4 Sair do Sistema' 
        print(opção_escolhida)
        break 
        
    
















