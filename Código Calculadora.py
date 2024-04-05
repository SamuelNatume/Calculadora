# Subtração
def subtract(x, y):
    return x - y

# Mltiplicação
def multiply(x, y):
    return x * y

# Divisão
def divide(x, y):
    if y == 0:
        return "Erro! Não pode divir por 0."
    else:
        return x / y

while True:
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")


    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha == '5':
        print("Você saiu!")
        break

    elif escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        

        if escolha == '1':
            print(num1, "+", num2, "=", num1 + num2)

        elif escolha == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Opção inválida!") 

