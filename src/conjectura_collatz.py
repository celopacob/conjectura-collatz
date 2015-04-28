#-*- coding: utf-8 -*-
import sys

def decompoe_numero(numero):
    counter = 1
    while (numero > 1):
        if int(numero) % 2 == 0:
            numero = numero/2
        else:
            numero = (3 * numero) + 1
        counter = counter + 1
    return counter

def execute(numero):
    larger_sequence_numero = 0
    larger_sequence = 0
    for i in range(numero):
        sequence = decompose_numero(i)
        if sequence > larger_sequence:
            larger_sequence = sequence
            larger_sequence_numero = i
    print larger_sequence_numero

def main():
    numero = int(sys.argv[1])
    execute(numero)

if __name__ == '__main__':
    main()