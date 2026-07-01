Lista = []
while True:
    operacao = str(input("Digite I (para iniciar) ou S (para sair): "))

    if operacao == "I" or operacao == "i":
        matricula = str(input("Digite o seu matricula: "))
        aluno = str(input("Digite o seu aluno: "))
        nota1 = float(input("Digite sua nota 1: "))
        nota2 = float(input("Digite sua nota 2: "))
        media = (nota1 + nota2) / 2
        situacao = "Aprovado" if media >= 7 else "Reprovado"

        dados = {matricula, aluno, media, situacao }

        Lista.append(dados)

    elif operacao == "S" or operacao == "s":
        print("----------------FICHA----------------")
        print("MATRICULA | ALUNO  |  NOTA | SITUAÇÃO")
        print(Lista)

        break