import math

# Entrada de dados com validação
quantidade_alunos = None

# Loop para garantir que a quantidade de alunos seja um número inteiro válido
while quantidade_alunos is None:
    try:
        entrada_quantidade = input("Quantos alunos deseja analisar? ")
        
        # Verifica se a entrada está vazia
        if entrada_quantidade.strip() == "":
            print("Erro: Digite um número válido!\n")
            continue
        
        quantidade_alunos = int(entrada_quantidade)
        
        # Verifica se é um número positivo
        if quantidade_alunos <= 0:
            print("Erro: A quantidade de alunos deve ser maior que zero!\n")
            quantidade_alunos = None
    
    except ValueError:
        print("Erro: Digite um número inteiro válido!\n")

notas_alunos = []

# Coleta das notas com validação
for i in range(quantidade_alunos):
    nota_valida = False
    
    # Loop até conseguir uma nota válida entre 0 e 10
    while not nota_valida:
        try:
            entrada_nota = input(f"Digite a nota do aluno {i + 1} (0 a 10): ")
            
            # Verifica se a entrada está vazia
            if entrada_nota.strip() == "":
                print("Erro: Digite uma nota válida!\n")
                continue
            
            nota = float(entrada_nota)
            
            # Verifica se a nota está entre 0 e 10
            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10!\n")
                continue
            
            notas_alunos.append(nota)
            nota_valida = True
        
        except ValueError:
            print("Erro: Digite um número válido (use ponto para decimais)!\n")

# Função para calcular a média
def calcular_media(lista_notas):
    soma_notas = sum(lista_notas)
    media = soma_notas / len(lista_notas)
    return media

# Função para calcular a mediana
def calcular_mediana(lista_notas):
    # Ordena as notas em ordem crescente
    notas_ordenadas = sorted(lista_notas)
    quantidade = len(notas_ordenadas)
    
    # Se a quantidade de elementos for ímpar, retorna o do meio
    # Se for par, retorna a média dos dois do meio
    if quantidade % 2 == 1:
        mediana = notas_ordenadas[quantidade // 2]
    else:
        meio1 = notas_ordenadas[(quantidade // 2) - 1]
        meio2 = notas_ordenadas[quantidade // 2]
        mediana = (meio1 + meio2) / 2
    
    return mediana

# Função para calcular o desvio padrão (usa math.sqrt do módulo math)
def calcular_desvio_padrao(lista_notas):
    media = calcular_media(lista_notas)
    
    # Calcula a soma das diferenças ao quadrado
    soma_quadrados = sum((nota - media) ** 2 for nota in lista_notas)
    
    # Desvio padrão = raiz quadrada da média dos desvios ao quadrado
    variancia = soma_quadrados / len(lista_notas)
    desvio_padrao = math.sqrt(variancia)
    
    return desvio_padrao

# Função para contar aprovados e reprovados
def contar_aprovados_reprovados(lista_notas, nota_minima=7.0):
    aprovados = sum(1 for nota in lista_notas if nota >= nota_minima)
    reprovados = len(lista_notas) - aprovados
    return aprovados, reprovados

# Cálculos
media_turma = calcular_media(notas_alunos)
mediana_turma = calcular_mediana(notas_alunos)
desvio_padrao_turma = calcular_desvio_padrao(notas_alunos)
aprovados, reprovados = contar_aprovados_reprovados(notas_alunos)

# Exibição dos resultados
print("\n=== ESTATÍSTICAS DE NOTAS ===")
print(f"Média: {media_turma:.2f}")
print(f"Mediana: {mediana_turma:.2f}")
print(f"Desvio Padrão: {desvio_padrao_turma:.2f}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")