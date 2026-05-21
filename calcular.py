#!/bin/bash
import os

os.system('clear')

valor1 = input("Digite o primeiro valor: ")

while True:
    print("Agora escolha a operação:")
    print("[1] para adição")
    print("[2] para subtração")
    print("[3] para multiplicação")
    print("[4] para divisão")

    resp = input(": ")

    if resp not in ["1", "2", "3", "4"]:
        print("Valor inválido! Tente novamente.\n")
    else:
        break

valor2 = input("Digite o segundo valor:")

valor1 = int(valor1)
valor2 = int(valor2)

if resp in["1"]:
  resultado = valor1 + valor2

if resp in["2"]:
  resultado = valor1 - valor2

if resp in["3"]:
  resultado = valor1 * valor2

if resp in["4"]:
  resultado = valor1 / valor2

print("Resultado: ",resultado)
