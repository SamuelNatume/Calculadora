# adição

def Soma(x,y):
    return x + y

# Subtração
def Subtração(x, y):
    return x - y

# Mltiplicação
def Multiplicação(x, y):
    return x * y

# Divisão
def Divisão(x, y):
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
            print(num1, "+", num2, "=", Soma(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", Subtração(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", Multiplicação(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", Divisão(num1, num2))
    else:
        print("Opção inválida!") 

