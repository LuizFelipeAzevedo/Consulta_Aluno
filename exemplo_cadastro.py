import datetime

def cadastro():
    nome = input("Nome: ")
    rm = int(input("RM: "))
    turma = input("Turma: ")
    data = input("Nascimento: ")
    aluno = {}
    aluno['nome'] = nome
    aluno['rm'] = rm
    aluno['turma'] = turma

    #quebrando a data e criando um objeto datetime
    (dia, mes, ano) = data.split('/')
    nascimento = datetime.datetime(int(ano), int(mes), int(dia))
    aluno["nascimento"] = nascimento

    return aluno

def altera(estudante):
    nome = input(f"Nome ({estudante['nome']}): ")
    if len(nome) > 0:
        estudante['nome'] = nome

    rm = input(f"RM ({estudante['rm']}): ")        
    if len(rm) > 0:
        estudante['rm'] = int(rm)

    turma = input(f"Turma ({estudante['turma']}): ")        
    if len(turma) > 0:
        estudante['turma'] = turma

def menu():
    print("Sistema estudantil: ")
    print("1 - cadastro aluno")
    print("2 - apaga aluno")
    print("3 - altera aluno")
    print("5 - sair do sistema")
    return int(input("Opção: "))

#programa principal
repositorio = []

opcao = menu()
while opcao != 5:
    if opcao == 1:
        aluno = cadastro()
        repositorio.append(aluno)
        print('Aluno cadastrado com sucesso!')
    elif opcao == 2:
        print('Removendo aluno')
        rm = int(input("RM: "))
        apagado = False
        i = 0
        while not apagado and i < len(repositorio):
            aluno = repositorio[i]
            if aluno['rm'] == rm:
                repositorio.pop(i)
                apagado = True
            i = i + 1
    elif opcao == 3:
        rm = int(input("Informe o rm: "))
        i = 0
        aluno = {}
        while i < len(repositorio):
            aluno = repositorio[i]
            if aluno['rm'] == rm:
                break
            i = i + 1

        if i < len(repositorio):
            altera(aluno)
        else:
            print("aluno nao encontrado")

    opcao = menu()