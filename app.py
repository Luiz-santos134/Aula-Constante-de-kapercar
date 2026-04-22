# colocar no github e no colab o codigo da aula e subir para o ava com o print do colab e github


# resolver algoritimo da constante de kaprecar, subir para o GitHub (publico) e para o ava, em pdf

numeros = []

while True:
    num = str(input("Digite um número inteiro com 4 digitos, com pelo menos 2 diferentes: "))

    if not (int(num) > 999 and int(num) < 9999) or not num.isdigit():
        print("Número inválido. Por favor, digite um número inteiro com 4 dígitos, com pelo menos 2 diferentes.")
        continue

    while int(num) != 6174:
        numeros=[]
        for algarismo in num:
            numeros.append(algarismo)

        crescendo = sorted(numeros) #faz uma lista com os algarismos do numero em ordem crescente
        descrescendo = sorted(numeros, reverse=True) #faz uma lista com os algarismos do numero em ordem decrescente, o reverse=True inverte a ordem da lista

        num1, num2, num3, num4 = crescendo
        numeroInteiro = str(num1) + str(num2) + str(num3) + str(num4)
        # print(numeroInteiro)

        num5, num6, num7, num8 = descrescendo
        numeroInteiro2 = str(num5) + str(num6) + str(num7) + str(num8)
        # print(numeroInteiro2)

        operacao = int(numeroInteiro2) - int(numeroInteiro)
        num = str(operacao).zfill(4) #zfill para preencher com zeros a esquerda caso o resultado seja menor que 4 digitos
        print(operacao)
        

    print('Parabéns, você chegou na constante de Kaprecar!')
    break
