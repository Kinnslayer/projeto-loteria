from random import sample

def lista_loto_facil(tamanho = 1):

    for i in range(tamanho):
        sub_lista_loto = []

        for i in range(1):
            sub_lista_loto = ((sample(range(1,26),15)))

        x = str (sub_lista_loto)
        x = x.replace("[","")
        x = x.replace("]","")
        sub_lista_loto = x

    return sub_lista_loto

def lista_quina(tamanho = 1):

    for i in range(tamanho):
        sub_lista_quina = []

        for i in range(1):
            sub_lista_quina = ((sample(range(1,81),5)))

        x = str(sub_lista_quina)
        x = x.replace("[", "")
        x = x.replace("]", "")
        sub_lista_quina = x

    return sub_lista_quina

def lista_mega_sena(tamanho = 1):

    for i in range(tamanho):
        sub_lista_mega = []

        for i in range(1):
            sub_lista_mega = ((sample(range(1,61),6)))

        x = str(sub_lista_mega)
        x = x.replace("[", "")
        x = x.replace("]", "")
        sub_lista_mega = x

    return sub_lista_mega

def menu():

     menu_loteria = int(input(""""========Loterias Python========"
        \nEscolha seu jogo:
        1 - Lotofácil
        2 - Quina
        3 - Mega Sena
        \nDigite o número correspondente ao jogo preterido: """))

     if menu_loteria == 1:
         print("Esses são os seus 15 números da Lotofácil: ", lista_loto_facil())

     elif menu_loteria == 2:
         print("Esses são os seus 5 números da quina: ", lista_quina())

     elif menu_loteria == 3:
         print("Esses são os seus 6 números da Mega Sena: ", lista_mega_sena())

     else:
         print("Número inválido! Escolha seu jogo novamente.")

     return menu()

