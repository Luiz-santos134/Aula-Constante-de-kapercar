# colocar no github e no colab o codigo da aula e subir para o ava com o print do colab e github


# resolver algoritimo da constante de kaprecar, subir para o GitHub (publico) e para o ava, em pdf

numeros = []

while True:
    num = str(input("Digite um número inteiro com 4 digitos, com pelo menos 2 diferentes: "))

    if int(num) > 999:
        print('entrou')
        for algarismo in num:
            numeros.append(int(algarismo))

        crescendo = sorted(numeros)
        descrescendo = sorted(numeros, reverse=True)

        num1, num2, num3, num4 = crescendo
        print(num1,num2, num3, num4)

        num5, num6, num7, num8 = descrescendo
        print(descrescendo)

        # resultado = descrescendo (crescendo)
        # print(resultado)

        
        break
    else:
        print('Número inválido! Digite um número inteiro com 4 dígitos, com pelo menos 2 diferentes.')


# lista = [20, 30, 40, 10]

# print(sorted(lista))

# print(sorted(lista, reverse=True))