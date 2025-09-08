
historico = []

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calculadora():
    while True:
        print("1. Soma")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividi")
        print("5. Ver histórico")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == "6":
            print("\nSaindo da calculadora...")
            print("\n--- HISTÓRICO DE RESULTADOS ---")
            for i, resultado in enumerate(historico, 1):
                print(f"{i}. {resultado}")
            break
        elif opcao == "5":
            print("\n--- HISTÓRICO DE RESULTADOS ---")
            if not historico:
                print("Nenhum cálculo realizado ainda.")
            else:
                for i, resultado in enumerate(historico, 1):
                    print(f"{i}. {resultado}")
            continue

        elif opcao in ["1", "2", "3", "4"]:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = somar(a, b)
                elif opcao == "2":
                    resultado = subtrair(a, b)
                elif opcao == "3":
                    resultado = multiplicar(a, b)
                elif opcao == "4":
                    resultado = dividir(a, b)

                print(f"Resultado: {resultado}")
                historico.append(resultado)

        else:
            print("Opção inválida. Tente novamente.")

calculadora()
