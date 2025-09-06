
laboratório = {
    '001': {
        'hostname': 'lab01-pc1',
        'config': ('Intel i5', '8 GB', '1 TB'),
        'status': {'usuario_logado': 'Gabriel', 'sistema_operacional': 'Windows 11', 'ligado': True}
    },
            
    '002': {
        'hostname': 'lab01-pc2',
        'config': ('AMD Ryzen 5', '16 GB', '512 GB SSD'),
        'status': {'usuario_logado': 'Ana', 'sistema_operacional': 'Windows 11', 'ligado': False}
    },

    '003': {
        'hostname': 'lab01-pc3',
        'config': ('Snapdragon 8', '4 GB', '256 GB SSD'),
        'status': {'usuario_logado': 'Amanda', 'sistema_operacional': 'macOS', 'ligado': False}
    },
    
    '004': {
        'hostname': 'lab01-pc4',
        'config': ('M2', '32 GB', '1 TB SSD'),
        'status': {'usuario_logado': 'Lucas Beija Mordendo', 'sistema_operacional': 'Windows 11', 'ligado': True}
    },
}

def exibir_menu():
    print('''1. Cadastrar computador
    2. Listar todos os computadores cadastrados
    3. Mostrar informações de um computador
    4. Gerenciar lista de manutenção (máx 6 computadores)
    5. Sair do programa''')
    return input("Escolha uma opção: ")

# Loop principal do menu
while True:
    opcao = exibir_menu()

if opcao == "1":
    cadastrar_computador()
elif opcao == "2":
    listar_computadores()
elif opcao == "3":
    mostrar_informacoes_computador()
elif opcao == "4":
    gerenciar_manutencao()
elif opcao == "5":
    print("Saindo do programa...")

else:
    print("Opção inválida. Tente novamente.")