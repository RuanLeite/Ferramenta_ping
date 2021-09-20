import os #Importa o módulo ou biblioteca os (integra os programas e 
#recursos do S.O)

print("#" * 60)#imprime 60 vezes #

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
#Variavel que vai receber do usuário o IP

print("-" * 60)#imprime 60 vezes -
os.system('ping -n 6 {}'.format(ip_ou_host))#chamando system da biblioteca os
#comando ping -n #numero de pacotes a ser enviado

print("-" * 60)#imprime 60 vezes -