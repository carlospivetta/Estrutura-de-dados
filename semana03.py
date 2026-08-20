class No:
    def __init__(self, valor: float):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_item(self, valor: float):
        novo_no = No(valor)
        
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            
        print(f"Item {valor} inserido com sucesso!")

    def listar_itens(self):
        if self.inicio is None:
            print("A lista está vazia.")
            return
        
        print("\n--- Itens na Lista ---")
        atual = self.inicio
        posicao = 1
        while atual is not None:
            print(f"[{posicao}] {atual.valor}")
            atual = atual.proximo
            posicao += 1

    def remover_item(self, valor: float):
        if self.inicio is None:
            print("A lista está vazia. Nada a remover.")
            return

        atual = self.inicio
        anterior = None

       
        while atual is not None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo

        
        if atual is None:
            print(f"Valor {valor} não encontrado na lista.")
            return

       
        if anterior is None:
            self.inicio = atual.proximo
        else:
          
            anterior.proximo = atual.proximo

        print(f"Item {valor} removido com sucesso!")


def main():
    lista = ListaEncadeada()
    
    while True:
        print("\n=====================")
        print("        MENU         ")
        print("=====================")
        print("1. Inserir item")
        print("2. Listar itens")
        print("3. Remover item")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor float a inserir: "))
            lista.inserir_item(valor)
                
        elif opcao == '2':
            lista.listar_itens()
            
        elif opcao == '3':
            valor = float(input("Digite o valor float a remover: "))
            lista.remover_item(valor)
                
        elif opcao == '0':
            print("Saindo do programa...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
