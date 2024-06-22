# consultas.py

import datetime
from pacientes import pacientes

agendamentos = []


def marcar_consulta():
    """Marca uma consulta para um paciente existente."""
    if not pacientes:
        print("Não há pacientes cadastrados.")
        return

    listar_pacientes()
    try:
        escolha = int(input("Escolha o número do paciente: ")) - 1
        if escolha < 0 or escolha >= len(pacientes):
            print("Paciente inválido!")
            return
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        return

    dia = input("Dia da consulta (DD/MM/AAAA): ")
    hora = input("Hora da consulta (HH:MM): ")
    especialidade = input("Especialidade: ")

    try:
        data_consulta = datetime.datetime.strptime(dia + " " + hora, '%d/%m/%Y %H:%M')
        if data_consulta < datetime.datetime.now():
            print("Não é possível agendar consultas retroativas!")
            return
    except ValueError:
        print("Data ou hora inválida! Tente novamente.")
        return

    if any(a['data'] == data_consulta for a in agendamentos):
        print("Consulta já agendada para este dia e horário!")
        return

    agendamentos.append({
        'paciente': pacientes[escolha],
        'data': data_consulta,
        'especialidade': especialidade
    })
    print("Consulta marcada com sucesso")


def cancelar_consulta():
    """Cancela uma consulta agendada."""
    if not agendamentos:
        print("Não há consultas agendadas.")
        return

    for idx, agendamento in enumerate(agendamentos, start=1):
        data_str = agendamento['data'].strftime('%d/%m/%Y %H:%M')
        print(f"{idx}. {agendamento['paciente']['nome']} - {data_str} - {agendamento['especialidade']}")

    try:
        escolha = int(input("Escolha o número da consulta para cancelar: ")) - 1
        if escolha < 0 or escolha >= len(agendamentos):
            print("Consulta inválida!")
            return
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        return

    agendamento = agendamentos[escolha]
    data_str = agendamento['data'].strftime('%d/%m/%Y %H:%M')
    confirmacao = input(
        f"Tem certeza que deseja cancelar a consulta de {agendamento['paciente']['nome']} em {data_str} "
        f"para {agendamento['especialidade']}? (s/n): ")

    if confirmacao.lower() == 's':
        agendamentos.pop(escolha)
        print("Consulta cancelada com sucesso")
    else:
        print("Cancelamento abortado")


def listar_pacientes():
    """Lista todos os pacientes cadastrados."""
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"{idx}. {paciente['nome']} - {paciente['telefone']}")
