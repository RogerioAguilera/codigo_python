

a = float (input ('Primeiro bimestre: '))
b= float (input( 'Segundo bimestre: '))
c = float (input('Terceiro bimestre: '))
d = float (input('Quarto bimestre: '))

media = (a+b+c+d) /4
if a <=10 and b <=10 and c<=10 and d<=10:
    print('media : {}'.format(media))
else:
    print ('Foi informado alguma nota inválida')


# a = float (input('Entre com um valor: '))
# b = float(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a ==0 or not resto_b >0:
#     print('foi digitado um numero par')
# else:
#     print ('nenhum numero par foi digitado')

# a = int(input('Primeiro valor: '))
# b= int(input ('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a >b and a > c:
#     print(' O maior número é {}' .format(a))
# elif b>a and b>c:
#     print('o maior número é b {}' . format(b))
# else:
#     print(' O maior numero e {}' .format(c))
# print ('final do programa')

# a = 0
# resultado = 'neutro'
# if a > 0:
#     resultado = 'positivo'
# elif a < 0:
#     resultado = 'negativo'
# a = resultado
# print (resultado)

# a = input('Digite o primeito valor: ')
# b = input('Digite o primeito valor: ')
# soma = a + b
# print('O valor da soma é: {soma}'.format(soma=soma))

# if not 5==5:
#     print('afirmação verdadeira')
# else:
#     print('afirmação falsa')

# a = 10
# b = 10
# c = 10
# if a > b or a >= c:
#     print('Primeiro afirmação é verdadeira')
# elif a == b:
#     print('Segunda afirmação é verdadeira')
# else:
#     print('Nenhuma afirmação é verdadeira')