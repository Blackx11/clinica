# pacientes.py


pacientes = []


def cadastrar_paciente():
    """Cadastra um novo paciente, verificando duplicidade pelo telefone."""
    nome = input("Nome do paciente: ")
    telefone = input("Telefone do paciente: ")

    # Verificar duplicidade
    if any(p['telefone'] == telefone for p in pacientes):
        print("Paciente já cadastrado!")
        return

    pacientes.append({'nome': nome, 'telefone': telefone})
    print("Paciente cadastrado com sucesso")


def listar_pacientes():
    """Lista todos os pacientes cadastrados."""
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"{idx}. {paciente['nome']} - {paciente['telefone']}")
