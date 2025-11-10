import os

# --- Estrutura de Dados ---
# Usando um dicionário para armazenar informações dos voos.
# Cada voo tem um destino, total de assentos e uma lista para as reservas.
voos = {
    "FM101": {
        "destino": "São Paulo",
        "total_assentos": 150,
        "reservas": []  # Lista para armazenar os nomes dos passageiros com reserva
    },
    "FM202": {
        "destino": "Rio de Janeiro",
        "total_assentos": 100,
        "reservas": ["John Doe", "Jane Smith"] # Reservas pré-existentes
    },
    "FM303": {
        "destino": "Bacabeira",
        "total_assentos": 120,
        "reservas": []
    }
}

def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    print("*" * 40)
    print("✈️  Sistema de Reservas FlyMeToTheMoon  ✈️")
    print("*" * 40)

def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n--- Menu Principal ---")
    print("1. Registrar uma Reserva")
    print("2. Verificar Disponibilidade de Assentos")
    print("3. Listar Todas as Reservas de um Voo")
    print("4. Sair")

def limpar_tela():
    """Limpa a tela do console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def aguardar_usuario():
    """Pausa a execução e aguarda o usuário pressionar Enter."""
    input("\nPressione Enter para voltar ao menu principal...")

def listar_voos_disponiveis():
    """Exibe a lista de voos disponíveis."""
    print("\n--- Voos Disponíveis ---")
    for codigo_voo, detalhes in voos.items():
        print(f"Voo {codigo_voo} para {detalhes['destino']}")

def registrar_reserva():
    """Gerencia a lógica para registrar um novo passageiro em um voo."""
    limpar_tela()
    print("--- Registrar Nova Reserva ---")
    listar_voos_disponiveis()
    
    codigo_voo = input("\nDigite o código do voo: ").upper()

    # Verificação condicional: O voo existe?
    if codigo_voo in voos:
        voo = voos[codigo_voo]
        assentos_disponiveis = voo["total_assentos"] - len(voo["reservas"])

        # Verificação condicional: Há assento disponível? (Evita overbooking)
        if assentos_disponiveis > 0:
            nome_passageiro = input("Digite o nome completo do passageiro: ")
            voo["reservas"].append(nome_passageiro)
            print(f"\n Sucesso! Reserva para {nome_passageiro} no voo {codigo_voo} confirmada.")
        else:
            print(f"\n Erro: O voo {codigo_voo} está lotado. Não há assentos disponíveis.")
    else:
        print(f"\n Erro: Código de voo '{codigo_voo}' não encontrado.")
    
    aguardar_usuario()

def verificar_disponibilidade():
    """Verifica e exibe a disponibilidade de assentos para um voo específico."""
    limpar_tela()
    print("--- Verificar Disponibilidade de Assentos ---")
    listar_voos_disponiveis()

    codigo_voo = input("\nDigite o código do voo para verificar: ").upper()

    if codigo_voo in voos:
        voo = voos[codigo_voo]
        assentos_reservados = len(voo["reservas"])
        total_assentos = voo["total_assentos"]
        assentos_disponiveis = total_assentos - assentos_reservados

        print("\n--- Status do Voo ---")
        print(f"Voo: {codigo_voo} para {voo['destino']}")
        print(f"Total de Assentos: {total_assentos}")
        print(f"Assentos Reservados: {assentos_reservados}")
        print(f"Assentos Disponíveis: {assentos_disponiveis}")
    else:
        print(f"\n Erro: Código de voo '{codigo_voo}' não encontrado.")

    aguardar_usuario()

def listar_reservas():
    """Lista todos os passageiros com reservas em um voo específico."""
    limpar_tela()
    print("--- Listar Reservas do Voo ---")
    listar_voos_disponiveis()

    codigo_voo = input("\nDigite o código do voo para listar as reservas: ").upper()

    if codigo_voo in voos:
        voo = voos[codigo_voo]
        print(f"\n--- Reservas para o Voo {codigo_voo} para {voo['destino']} ---")
        
        # Estrutura de repetição: Percorre as reservas se existirem
        if voo["reservas"]:
            for i, passageiro in enumerate(voo["reservas"], 1):
                print(f"{i}. {passageiro}")
        else:
            print("Nenhuma reserva encontrada para este voo.")
    else:
        print(f"\n Erro: Código de voo '{codigo_voo}' não encontrado.")

    aguardar_usuario()

def main():
    """Função principal para executar o loop da aplicação."""
    # Estrutura de repetição: O loop principal do programa
    while True:
        limpar_tela()
        exibir_cabecalho()
        exibir_menu()
        
        escolha = input("\nEscolha uma opção (1-4): ")

        if escolha == '1':
            registrar_reserva()
        elif escolha == '2':
            verificar_disponibilidade()
        elif escolha == '3':
            listar_reservas()
        elif escolha == '4':
            print("\nObrigado por usar o sistema FlyMeToTheMoon. Adeus! 👋")
            break # Sai do loop while
        else:
            print("\nOpção inválida. Por favor, digite um número entre 1 e 4.")
            aguardar_usuario()

if __name__ == "__main__":
    main()
