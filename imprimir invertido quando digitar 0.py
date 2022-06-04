# Lista de valores:
seq = []

# Executa até ocorrer `break`
while True:

    # Pede ao usuário um valor inteiro:
    n = int(input("Digite n: "))    

    # Se for zero, pare o loop:
    if n == 0: break

    # Se não, adiciona o valor a lista:
    seq.append(n)

# Percorre toda a lista de trás para frente:
for i in reversed(seq):

    # Exibe o valor na tela:
    print(i)
