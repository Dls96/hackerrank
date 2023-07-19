# Problema: Dada uma lista de 5 inteiros positivos, ache os menores e os maiores valores que podem ser calculadas
# Somando exatamente 4 valores desta lista, então mostre na tela o resultado da minima e maxima respectivamente na mesma linha.  

#!/bin/python3
import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    # Arranjando os valores da lista em ordem crescente
    arr = sorted(arr)

    # variáveis que irão guardar o resultado da soma mínima e máxima
    min_sum = max_sum = 0

    # como está sortido do menor para o maior valor, 
    # é so pegarmos os 4 primeiros para saber a menor soma possível
    for i in range(4):
        min_sum += arr[i]

    # na mesma lógica para sabermos a maior soma 
    # é so pegarmos os 4 últimos valores da lista
    for i in range(1, 5):
        max_sum += arr[i]
    
    # mostra na tela o resultado de cada na mesma linha, separada por 1 espaço
    print(f'{min_sum} {max_sum}')
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
