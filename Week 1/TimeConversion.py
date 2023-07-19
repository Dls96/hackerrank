# Problema: Dado um horário em um formato 12-horas AM/PM, converta para 24-horas
# Obs: 12:00:00AM é 00:00:00 em um relógio 24-horas 
#    e 12:00:00PM é 12:00:00 em um relógio 24-horas

#!/bin/python3

import math
import os
import random
import re
import sys



def timeConversion(s):
    # Write your code here
    # extrai os 2 primeiros valores da string s e converte em int, que são as horas
    # e é o que queremos converter
    hour = int(s[0:2])

    # variável que irá guardar o horário restante, sem as horas
    res = s[2::]

    # se o horário estiver em AM
    if 'AM' in s:
        # verificamos se a hora está entre 1 e 11 
        if hour > 0 and hour < 12:
            # aqui não vamos precisar mexer em nada, somente tiramos a palavra AM
            return s.replace('AM', '')
        else:
            # se a hora for 12 então fazemos a conversão
            # adicionamos o 00 aos ultimos 6 valores da string res, que seriam :00:00
            return '00' + res[:6]

    # se o horário estiver em PM
    else:
        # verificamos se a hora está entre 1 e 11 
        if hour > 0 and hour < 12:
            # adicionamos mais 12 horas ao horário atual 
            # e concatenamos aos últimos 6 valores da string
            return f'{hour + 12}' + res[:6]
        else:
            # se a hora for 12, então deixamos como está 
            return s.replace('PM', '')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()