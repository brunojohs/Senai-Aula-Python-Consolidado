
===========================================================================================
# Auto: Bruno Manoel
# Data: 28/05/2024
# Versão: 1.0
# Objetivo: Temperatura
# Descrição:       Faça um algorítimo que receba a temperatura em °C 
#                  e converta para °F e °K
#
#               ------------------------------------
#               Exemplo de Execução:    
#               Insira a temperatura em Celsius: 0
#               Fahrenheit: 32
#               Kelvin: 273.15
#               ------------------------------------

# variaveis: 
celsius = 0 # temperatura sem Celsius inserida pelo usuário
Fahrenheit = 0 # temperatura sem Fahrenheit vinda da conversão
kelvin = 0  

# entrada
celsius = float (input('insira a temperatura em celsius:'))
Fahrenheit = (celsius * (9/5) + 32)
kelvin = celsius + 273.15

# saída

print(celsius,'°C equivalem ',Fahrenheit '°F') 
print(celsius,'°C equivalem ',kelvin'K')

                   

