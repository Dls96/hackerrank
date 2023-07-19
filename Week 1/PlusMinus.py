# Problema: Dado um array de inteiros, calcule a proporção dos elementos que são positivos, negativos e zero. 
# mostre na tela o valor de cada fração em uma linha nova, com 6 casas após a virgula


import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Write your code here
    # criando as variáveis que irão guardar a quantidade de valores positivos, negativos e zero.
    qtd_positive = qtd_negative = qtd_zero = 0

    # para cada valor que há na lista arr
    for i in arr:
        # verifica se o valor atual da lista é menor que zero, se sim adiciona 1 à variável n_negative
        if i < 0:
            qtd_negative +=1
        # se o valor for maior que zero, adiciona 1 à varíavel n_positive
        elif i > 0:
            qtd_positive += 1
        
        # se o valor for zero, adiciona 1 à variável n_zero
        else:
            qtd_zero += 1

    # mostra na tela a porporção de cada fração, com 6 casas após a virgula
    print('{:.6f}'.format(qtd_positive/len(arr)))
    print('{:.6f}'.format(qtd_negative/len(arr)))
    print('{:.6f}'.format(qtd_zero/len(arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)