# coding=utf-8
from time import sleep
import sys
import random

interativo = False

premios=[]
for i in range(6):
    premios.append('Squeeze')

premios.append('Mochila')

pessoas = []
pessoas.append("Kaanya")
pessoas.append("Daniel")
pessoas.append("Marcelo")
pessoas.append("Mateus")
pessoas.append("Taison")
pessoas.append("Italberto")
pessoas.append("Maurílio")
pessoas.append("Francisco")
pessoas.append("Ronivon")
pessoas.append("Cledjan")
pessoas.append("Joelson")
pessoas.append("Pacheco")
pessoas.append("Péricles")
pessoas.append("Anatália")
pessoas.append("Brandão")
pessoas.append("Arinaldo")
pessoas.append("Felipe")

resposta = 'sim'

resultado = {}

def print_extrato(premios):
    print("Ainda restam {} prêmios para sorteio.".format(len(premios)))
    print("-----------------")
    for p in premios:
        print("\t{}".format(p))

def suspense():

    linha = '......................\n'
    for x in linha:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)

def wait(palavra="sortear"):
    input("\nPressione [Enter] para {}...".format(palavra))

def sorteio(interativo):
    premio = premios[0]
    sys.stderr.write("\x1b[2J\x1b[H")
    print('-------------------------------------------------------')
    print("\nO próximo prêmio sorteado será um(a): >>>{}<<<".format(premio))

    wait()

    suspense()

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

print("Serão sorteados {} itens, entre {} participantes.".format(len(premios),len(pessoas)))
wait("iniciar")

if interativo:
    while (resposta.lower() == 'sim' or resposta.lower() == 's') and (len(premios)>0):
         resposta = sorteio(interativo)
else:
    while (len(premios)>0):
         resposta = sorteio(interativo)


print("\nResultado final do sorteio.")
for i in resultado.keys():
    print("\t{} ganhou um(a) {}.".format(i,resultado[i]))
