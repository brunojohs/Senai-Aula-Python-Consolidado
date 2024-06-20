# Autor: Bruno Manoel
# Data: 114/06/2024
# Versão: 1.0
# Objetivo: Exercício 8 - Sistema para receber senha do usuário  
# Descrição   : 
#===========================================================

senha = '' # Variável para receber a senha do usuário
senhaPadrao = 'senha115'
tentativas = 3 # Numero de tentativas

while True:
    senha = input('digita a sua senha: ') # Senha 115 -> numeros com letras

    if senha == senhaPadrao:
        print('Acesso liberado')
        break # quebra o loop while, ou seja finalizado o programa

    else:
        tentativas = tentativas - 1
        print('Voce só possui mais' , tentativas, 'tentativas' )    
        
    if  tentativas <= 0:
        print('não possui mais tentativas')
        break
