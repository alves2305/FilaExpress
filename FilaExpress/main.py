from lista_encadeada import ListaEncadeada

def menu():
    lista = ListaEncadeada()
    while True:
        print("1- Adicionar paciente à fila")
        print("2- Mostrar pacientes na fila")
        print("3- Chamar paciente")
        print("4- Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            lista.inserir()
        elif opcao == 2:
            lista.imprimirListaEspera()
        elif opcao == 3:
            lista.atenderPaciente()
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()