# Agenda de Festas de Animação

class Festa:
    def __init__(self, nome, data, hora, local, descricao):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.local = local
        self.descricao = descricao

class Agenda:
    def __init__(self):
        self.festas = []

    def adicionar_festa(self, festa):
        self.festas.append(festa)

    def remover_festa(self, nome_festa):
        for festa in self.festas:
            if festa.nome == nome_festa:
                self.festas.remove(festa)
                print(f"Festa '{nome_festa}' removida com sucesso!")
                return
        print(f"Festa '{nome_festa}' não encontrada.")

    def listar_festas(self):
        print("Festas agendadas:")
        for festa in self.festas:
            print(f"  {festa.nome} - {festa.data} {festa.hora} - {festa.local} - {festa.descricao}")

    def buscar_festa(self, nome_festa):
        for festa in self.festas:
            if festa.nome == nome_festa:
                print(f"Festa '{nome_festa}' encontrada:")
                print(f"  Data: {festa.data}")
                print(f"  Hora: {festa.hora}")
                print(f"  Local: {festa.local}")
                print(f"  Descrição: {festa.descricao}")
                return
        print(f"Festa '{nome_festa}' não encontrada.")

def main():
    agenda = Agenda()

    while True:
        print("Menu:")
        print("  1. Adicionar festa")
        print("  2. Remover festa")
        print("  3. Listar festas")
        print("  4. Buscar festa")
        print("  5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da festa: ")
            data = input("Digite a data da festa (DD/MM/YYYY): ")
            hora = input("Digite a hora da festa (HH:MM): ")
            local = input("Digite o local da festa: ")
            descricao = input("Digite a descrição da festa: ")
            festa = Festa(nome, data, hora, local, descricao)
            agenda.adicionar_festa(festa)
            print("Festa adicionada com sucesso!")
        elif opcao == "2":
            nome_festa = input("Digite o nome da festa para remover: ")
            agenda.remover_festa(nome_festa)
        elif opcao == "3":
            agenda.listar_festas()
        elif opcao == "4":
            nome_festa = input("Digite o nome da festa para buscar: ")
            agenda.buscar_festa(nome_festa)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()