class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada =False
        else:
            self.ligada =True

    def aumenta_canal(self):
        self.canal +=1
        if self.ligada:
            self.canal +=1

    def diminui_canal(self):
        self.canal -=1
        if self.ligada:
            self.canal -=1


televisao = Televisao()
print (televisao.ligada)
televisao.power()
print(' A televisao está ligada: {} ' .format (televisao.ligada))
televisao.power()
print( ' A televisao está ligada: {} ' .format(televisao.ligada))
televisao.power()
print( ' A televisao está ligada: {} ' .format(televisao.ligada))
televisao.power()
print ('Canal:  {}' . format(televisao.canal))
televisao.aumenta_canal()
print ('Canal:  {}' . format(televisao.canal))
televisao.aumenta_canal()
print (' Canal : {} ' .format(televisao.canal))
televisao.diminui_canal()
print (' Canal : {} ' .format(televisao.canal)

# def minha_funcao(numero):
#     if numero % 2 == 0:
#         return '{} é par'.format(numero)
#     else:
#         return '{} é ímpar'.format(numero)
#     return "zero é neutro"
#
# resultado = minha_funcao(0)
# print(resultado)
#
#
# class Carro:
#     def __init__(self):
#         self.motor = 'desligado'
#         self.movimento = False
#
#     def ligar(self):
#         self.motor = 'ligado'
#
#     def acelerar(self):
#         if self.motor == 'ligado':
#             self.movimento = True
#
#     def carro_em_movimento(self):
#         return self.movimento
#
#
# # carro = Carro()
# # carro.acelerar()
# # carro_em_movimento = carro.carro_em_movimento()
# # print(carro_em_movimento)
#
# class Liquidificador:
#     def __init__(self):
#         self.velocidade = 0
#         self.power = False
#
#     def velocidade_A(self):
#         # lacuna1
#         if self.power:
#             self.velocidade = 1
#
#     def velocidade_B(self):
#         # lacuna2
#         if self.power:
#             self.velocidade = 2
#
#     def velocidade_Z(self):
#         self.velocidade = 0
#         self.power = 0


