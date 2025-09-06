
laboratório = {
    '001': {
        'hostname': 'lab01-pc1',
        'config': ('Intel i5', '32 GB', '1 TB'),
        'status': {'usuario_logado': 'Gabriel', 'sistema_operacional': 'Windows 11', 'ligado': True}
    },

    '002': {
        'hostname': 'lab01-pc2',
        'config': ('AMD Ryzen 5', '16 GB', '512 GB SSD'),
        'status': {'usuario_logado': 'Ana', 'sistema_operacional': 'Ubuntu', 'ligado': False}
    },

    '003': {
        'hostname': 'lab01-pc3',
        'config': ('Snapdragon 8', '4 GB', '256 GB SSD'),
        'status': {'usuario_logado': 'Amanda', 'sistema_operacional': 'Ubuntu', 'ligado': False}
    },

    '004': {
        'hostname': 'lab01-pc4',
        'config': ('M2', '32 GB', '1 TB SSD'),
        'status': {'usuario_logado': 'Lucas Beija Mordendo', 'sistema_operacional': 'macOS', 'ligado': True}
    },

    '005': {
        'hostname': 'lab01-pc5',
        'config': ('Intel i7', '16 GB', '512 TB SSD'),
        'status': {'usuario_logado': 'Lucas Beija Mordendo', 'sistema_operacional': 'Windows 11', 'ligado': True}
    },
}

lista_manutencao = []

def exibir_menu():
    print('''
    1. Cadastrar computador
    2. Listar todos os computadores cadastrados
    3. Mostrar informações de um computador
    4. Gerenciar lista de manutenção (máx 6 computadores)
    5. Sair do programa''')
    return input("Escolha uma opção: ")

def gerenciar_manutencao():
    print('''
    1. Criar/Limpar lista de manutenção
    2. Adicionar computador à lista
    3. Listar todos os computadores na lista
    4. Mostrar o primeiro computador da lista
    5. Mostrar o último computador da lista
    6. Mostrar o computador em um índice específico
    7. Remover um computador da lista''')
    gerenciar_manutencao = input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()
    if opcao == "1":
        cadastrar_computador()
    if opcao == "2":
        listar_computadores()
    if opcao == "3":
        informacoes_computador()
    if opcao == "4":
        gerenciar_manutencao()
        if gerenciar_manutencao == "1":
            lista_manutencao = []
            print("Lista de manutenção criada/limpa.")

        elif gerenciar_manutencao == "2":
            id_pc = input('Digite o id do computador que deseja adicionar: ')
            if id_pc in laboratório:
                if len(lista_manutencao) < 6:
                    lista_manutencao.append(laboratório[id_pc])
                    print(f"Computador {id_pc} adicionado à lista de manutenção.")
                else:
                        print("A lista de manutenção já está cheia (máx 6 computadores).")
            else:
                print("Computador não encontrado no laboratório.")

        elif gerenciar_manutencao == "3":
            if lista_manutencao:
                    for pc in lista_manutencao:
                        print(f"{pc['hostname']} - {pc['config']}")
            else:
                print("A lista de manutenção está vazia.")
                
        elif gerenciar_manutencao == "4":
            if lista_manutencao:
                primeiro_pc = lista_manutencao[0]
                print(f"Primeiro computador na lista: {primeiro_pc['hostname']} - {primeiro_pc['config']}")

        elif gerenciar_manutencao == "5":
            if lista_manutencao:
                ultimo_pc = lista_manutencao[-1]
                print(f"Último computador na lista: {ultimo_pc['hostname']} - {ultimo_pc['config']}")
                
        elif gerenciar_manutencao == "6":
            indice = int(input("Digite o índice do computador que deseja ver (0 a 5): "))
            if 0 <= indice < len(lista_manutencao):
                pc_especifico = lista_manutencao[indice]
                print(f"Computador no índice {indice}: {pc_especifico['hostname']} - {pc_especifico['config']}")
            else:
                print("Índice inválido ou fora do alcance da lista.")
                
        elif gerenciar_manutencao == "7":
            id_pc = input('Digite o id do computador que deseja remover: ')
            pc_para_remover = next((pc for pc in lista_manutencao if pc['hostname'].endswith(id_pc)), None)
            if pc_para_remover:
                lista_manutencao.remove(pc_para_remover)
                print(f"Computador {id_pc} removido da lista de manutenção.")
            else:
                print("Computador não encontrado na lista de manutenção.")

    if opcao == "5":
        print("Saindo do programa...")