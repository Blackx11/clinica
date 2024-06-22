# utils.py

def exibir_menu():
    """Exibe o menu principal e navega pelas opções do usuário."""
    print("\n--- Menu Principal ---")
    print("1. Cadastrar um paciente")
    print("2. Marcações de consultas")
    print("3. Cancelamento de consultas")
    print("4. Sair")


def obter_opcao():
    """Obtém a opção escolhida pelo usuário."""
    return input("Escolha uma opção: ")
