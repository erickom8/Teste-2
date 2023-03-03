#boa noite pessoal
opcao = 0
while (opcao != 1):
    if opcao == 0:
        arquivo = open("basedados.txt", "a")
        nome = input("Digite seu nome: ")
        numero = input("Digite seu numero: ")
        arquivo.write(nome+";"+numero+"\n")
        arquivo.close()
    elif opcao == 2:
        arquivo = open("basedados.txt", "r")
        for linha in arquivo:
            print(linha)
        arquivo.close()
    opcao = int(input("Deseja continuar? 1 - sair / 0 - cadastrar dado / 2 - executar"))
