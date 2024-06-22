# main.py
from pacientes import cadastrar_paciente
from consultas import marcar_consulta, cancelar_consulta
from utils import exibir_menu, obter_opcao


def menu_principal():
    """Exibe o menu principal e navega pelas opções do usuário."""
    while True:
        exibir_menu()
        opcao = obter_opcao()

        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            marcar_consulta()
        elif opcao == '3':
            cancelar_consulta()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
