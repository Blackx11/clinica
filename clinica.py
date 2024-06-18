import datetime

pacientes = []
agendamentos = []

def menu_principal():
    while True:
        print("1. Cadastrar um paciente")
        print("2. Marcações de consultas")
        print("3. Cancelamento de consultas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
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

def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    telefone = input("Telefone do paciente: ")
    
    # Verificar duplicidade
    for paciente in pacientes:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!")
            return
    
    pacientes.append({'nome': nome, 'telefone': telefone})
    print("Paciente cadastrado com sucesso")

def listar_pacientes():
    for idx, paciente in enumerate(pacientes):
        print(f"{idx + 1}. {paciente['nome']} - {paciente['telefone']}")

def marcar_consulta():
    if not pacientes:
        print("Não há pacientes cadastrados.")
        return
    
    listar_pacientes()
    escolha = int(input("Escolha o número do paciente: ")) - 1
    
    if escolha < 0 or escolha >= len(pacientes):
        print("Paciente inválido!")
        return
    
    dia = input("Dia da consulta (DD/MM/AAAA): ")
    hora = input("Hora da consulta (HH:MM): ")
    especialidade = input("Especialidade: ")
    
    data_consulta = datetime.datetime.strptime(dia + " " + hora, '%d/%m/%Y %H:%M')
    if data_consulta < datetime.datetime.now():
        print("Não é possível agendar consultas retroativas!")
        return
    
    for agendamento in agendamentos:
        if agendamento['data'] == data_consulta:
            print("Consulta já agendada para este dia e horário!")
            return
    
    agendamentos.append({
        'paciente': pacientes[escolha],
        'data': data_consulta,
        'especialidade': especialidade
    })
    print("Consulta marcada com sucesso")

def cancelar_consulta():
    if not agendamentos:
        print("Não há consultas agendadas.")
        return
    
    for idx, agendamento in enumerate(agendamentos):
        data_str = agendamento['data'].strftime('%d/%m/%Y %H:%M')
        print(f"{idx + 1}. {agendamento['paciente']['nome']} - {data_str} - {agendamento['especialidade']}")
    
    escolha = int(input("Escolha o número da consulta para cancelar: ")) - 1
    
    if escolha < 0 or escolha >= len(agendamentos):
        print("Consulta inválida!")
        return
    
    agendamento = agendamentos[escolha]
    data_str = agendamento['data'].strftime('%d/%m/%Y %H:%M')
    confirmacao = input(f"Tem certeza que deseja cancelar a consulta de {agendamento['paciente']['nome']} em {data_str} para {agendamento['especialidade']}? (s/n): ")
    
    if confirmacao.lower() == 's':
        agendamentos.pop(escolha)
        print("Consulta cancelada com sucesso")
    else:
        print("Cancelamento abortado")

menu_principal()
