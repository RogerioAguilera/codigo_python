from aula7_calculadora1 import Calculadora
from aula7_televisao import Televisao
from aula8_contador_letras import contador_letras


calculadora = Calculadora(5,10)
print(calculadora.soma())
televisao = Televisao()
televisao.power()
print(televisao.ligada)
lista=['cachorro', 'gato', 'elefante']
total_letras =contador_letras(lista)
print('total de letras por palavras na lista: {}' .format(total_letras))