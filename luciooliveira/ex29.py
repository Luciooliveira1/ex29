def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - Novo cadastro")
    print("Ver cadastro")
    print("3 - Sair")
    print("----------------------------------")

    def cadastrar_pessoa (cadastros):
        nome = input("nome:")
        idade = input("Idade:")
        turma = input("Turma:")
        curso = input("Curso:")
        cadastros.append({"Nome": nome, "idade": idade, "turma": turma, "cursos": curso,})
        print("Cadastro realizado com sucesso!")