# velocidade = int(input("Qual foi a sua velocidade"))
# if velocidade <=100:
#     multa = 0
# elif velocidade <= 120:
#     multa = velocidade * 0.2
# elif velocidade <=150:
#     multa = 120 * 0.2 + 0.3 *velocidade
# else:
#     multa = 0.2*120 + 0.3*150 + 4 *velocidade
#
# print(f"Sua multa será de R${multa:.2f}")


# lados =  int(input("Diga a quantidade de lados:"))
# forma = ''
# if lados < 3 :
#     print("poligono n indetificado")
# elif lados ==3:
#     forma = "quadrado"
# elif lados == 5:
#     forma = "pentagono"
# else:
#     print("poligono n indentificado ")
# if forma:
#     medida =  int(input("Diga o tamanho de lados:"))
#     perimetro = lados*medida
# print(f"vc escolheu o {forma} com perimetro de {perimetro}")


# lados =  int(input("Diga a quantidade de lados:"))
# if lados < 3 :
#     print("poligono n indetificado")
# elif lados > 5:
#     print("poligono n intentificado")
# else:
#     medida =  int(input("Diga o tamanho de lados:"))
#     if lados ==3:
#         forma= "triangulo "
#     elif lados == 4 :
#         forma= "quadrado"
#     else:
#         forma = "pentagono"



# n1 = int(input("digite um numero:"))
# n2= int(input("digite um numero:"))
# n3 = int(input("digite um numero:"))
# n4 = int(input("digite um numero:"))
# n5 = int(input("digite um numero:"))
#
# par = 0
#
# if n1%2==0:
#     par = 1
# if n2%2==0:
#     par = par +1
# if n3%2==0:
#     par = par +1
# if n4%2==0:
#     par = par +1
# if n5%2==0:
#     par = par +1
# print(f'tem {par} numeros pares')
# impar = 5 - par
# print(f'tem {impar} numeros impares')

# senha = input("Digite sua senha: ")
# senha_correta = '1234'
# qtd = 0
# while senha != senha_correta and qtd<3:
#     senha=input("Senha incorreta! Digite novamente: ")
#     qtd=qtd+1 #qtd +=1
# if qtd >2 :
#     print("acesso bloqueado ")
#
# else:
#     print("Senha correta")


# numero = 0
# soma= 0
# while numero < 10:
#     numero+=1
#     soma += numero
#     print(numero)
# print(f"Sua soma é: {soma}")

# i = 0
# impar = 0
# par= 0
# while i <10:
#     number =int(input(f"digite um numero"))
#     if number % 2 ==0:
#         par +=1
#     else:
#         impar +=1
#     i +=1
# print(f"Vc digitou {par} numeros pares e {impar} numeros impares")


# frase = input("vc é alto? ")
#
# while frase != 'sim' and frase != 'não':
#     frase=input("frase incorreta! Digite apenas sim ou não: ")
#
# print("correto")

# frase = input("vc é alto? ")
#
# while not frase == 'sim' or frase == 'não':
#     frase=input("frase incorreta! Digite apenas sim ou não: ")
#
# print("correto")

# a cada ano a popula~ção dobra nesse pais, ela começa com 100000 a cada ano *2 quantos anos para oassar de 1bi
populacao = 100000
ano = 0
while populacao <=1000000000:
    populacao *=2
    ano +=1
    print(ano)
    print(populacao)
print(f"atingiu 1 bi depois {ano} anos")
