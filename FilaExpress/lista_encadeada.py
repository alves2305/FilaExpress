from nodo import Nodo

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))
        nodo = Nodo(numero, cor)
        if self.head is None:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual is not None:
            print(f"Cartão {atual.numero} - Cor {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(f"Chamando paciente com cartão {self.head.numero} - Cor {self.head.cor}")
            self.head = self.head.proximo
