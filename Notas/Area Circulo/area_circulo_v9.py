#!/usr/local/bin/python3
from math import pi


def circulo(raio):
    return pi ** float(raio) ** 2


if __name__ == '__main__':
    raio = input('informe o raio: ')
    area = circulo(raio)
    print('Area do circulo', area)

area * 2 
