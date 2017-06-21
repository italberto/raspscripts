# coding=utf-8
# Autor: Italberto Figueira Dantas
# Descrição: Realiza o sorteio de itens entre os participantes informados em um arquivo txt.
#

from time import sleep
import sys
import random

# Imprime o extrato dos prêmios restantes.
def print_extrato(premios):
    print("Ainda restam {} prêmios para sorteio.".format(len(premios)))
    print("-----------------")
    for p in premios:
        print("\t{}".format(p))

#Imprime na tela um linha pontilhada "animada", só pra gerar suspense.
def suspense():
    linha = '......................\n'
    for x in linha:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)

# Aguarda a confirmação da ação de pressionar enter pra prosseguir o sorteio.
def wait(palavra="sortear"):
    input("\nPressione [Enter] para {}...".format(palavra))


#Método principal pra realizar o sorteio.
def sorteio(interativo):
    premio = premios[0]
    sys.stderr.write("\x1b[2J\x1b[H")
    print('-------------------------------------------------------')
    print("\nO próximo prêmio sorteado será um(a): >>>{}<<<".format(premio))

    wait()

    suspense()

    # Trecho que escolhe um número aleatório entre 0  e o tamanho da lista de participantes len(pessoas).
    sort = random.randint(0, len(pessoas) - 1)  # 5
    escolhido = pessoas[sort]
    print('Parabéns {} você ganhou um(a) {}!!!'.format(escolhido, premio))

    pessoas.remove(escolhido)
    premios.pop(0)

    resultado[escolhido] = premio

    print_extrato(premios)

    if interativo:
        return input("Deseja mais uma rodada? (Sim ou Não)  >")
    else:
        return ''




premios=[]
#Povoa a lista de prêmios.
for i in range(6):
    premios.append('Squeeze')
premios.append('Mochila')

#Abre o arquivo dos participantes.
arquivo_participantes = open('participantes.txt','r')
pessoas = []

#Lê as linhas do arquivo e coloca os participantes na lista.
for l in arquivo_participantes.readlines():
    pessoas.append(l.replace('\n', ''))

resposta = 'sim'

resultado = {}

print("Serão sorteados {} itens, entre {} participantes.".format(len(premios),len(pessoas)))
wait("iniciar")

#Caso deseje-se utilizar o sorteio interativo ou ñ interativo.
interativo = False
if interativo:
    while (resposta.lower() == 'sim' or resposta.lower() == 's') and (len(premios)>0):
         resposta = sorteio(interativo)
else:
    while (len(premios)>0):
         resposta = sorteio(interativo)


print("\nResultado final do sorteio.")
for i in resultado.keys():
    print("\t{} ganhou um(a) {}.".format(i,resultado[i]))
