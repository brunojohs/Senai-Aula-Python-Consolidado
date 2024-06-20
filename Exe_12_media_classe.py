# Autor: Bruno Manoel
# Data: 114/06/2024
# Versão: 1.0
# Objetivo: Exercício 12 - Média da Classe  
# Descrição   : Faça um programa que receba duas notas de seis alunoe 
#               Calcule e mostre:
#               A Média Aritimética das duas notas de cada aluno; e a mensagem da tabela a seguir: 
#                           Média Aritimética               Mensagem
#                                   Até 3                   Reprovado
#                             Entre 3 e 7                   Exame
#                             De 7 para cima                Aprovado
# 
#                           O Total de Alunos aprovados;
#                           O Total de Alunos de exames;
#                           O Total de alunos reprovados;
#                           A Médida da classe;
#                     
#===========================================================

#Aluno 1 

aluno = 0
qtdealunos = 6 # Esta variável limita a quantidade de notas (alunos) a serem inseridas
alunosaprovados = 0
alunosreprovados = 0
alunosexame = 0
mediaclasse = 0

while 
    aluno < qtdealunos:
    aluno = aluno + 1 # este parametro automatiza a contagem do próximo aluno
    nota_um = 0
    nota_dois = 0
    media = 0

    nota_um = float(input(f'Insira a nota 1 do Aluno {aluno}):'))
    nota_dois = float(input(f'Insira a nota 2 do Aluno {aluno}:'))

    media = (nota_um + nota_dois)/2 # Esta variável faz o cáculo da média

    if(media <=3):
        print('Reprovado')
        alunosreprovados +=1 # esta variável faz a contagem para contabilizar no total a ser calculado em alunos aprovados
        mediaclasse +=1


    elif(media >= 4 and media <=7):
        print('Exame')
        alunosexame +=1  # esta variável faz a contagem para contabilizar no total a ser calculado em alunos de Exames
        mediaclasse +=1

    else:
        print('Aprovado')
        alunosaprovados +=1 # esta variável faz a contagem para contabilizar no total a ser calculado em alunos de Aprovados
        mediaclasse +=1

print(f'Quantidade de alunos Aprovados:{alunosaprovados}')
print(f'Quantidade de alunos Reprovados:{alunosreprovados}')
print(f'Quantidade de alunos em Exame:{alunosexame}')




# Variaáveis

#notas = 0
#resultn1 = 0
#resultn2 = 0
#mediaaritimetica = 0 
#classificacao = ''

# Entrada 

#resultn1 = int (input('Aluno 1 Insira a sua nota 1 '))
#resultn2 = int (input('Aluno 1 Insira a sua nota 2 '))

# processamento

#if(mediaaritimetica > 0 and mediaaritimetica <= 3):
#   classificacao = 'Reprovado'

#elif(mediaaritimetica > 3 and mediaaritimetica <= 7):
#   classificacao = 'Exame'

#elif(mediaaritimetica >= 7 and mediaaritimetica <=10):
#   classificacao = 'Aprovado'

#saída
#   print (classificacao)




