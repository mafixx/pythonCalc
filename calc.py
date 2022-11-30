def soma(P, Q):
    return P + Q


def subtracao(P, Q):
    return P - Q


def multiplicacao(P, Q):
    return P * Q


def divisao(P, Q):
    return P / Q


print("Por favor, selecione a operação: ")
print("a. Soma")
print("b. Subtração")
print("c. Multiplicação")
print("d. Divisão")

choice = input("Escolha a operação (a/ b/ c/ d): ")

num_1 = int(input("Entre com o primeiro número: "))
num_2 = int(input("Entre com o segundo número: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", soma(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", subtracao(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiplicacao(num_1, num_2))

elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divisao(num_1, num_2))

else:
    print("Opção inválida!")