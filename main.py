"""Funções def """


#Cálculo de Média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

#Verificação de nota minima para aprovação
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#validação de nota para aceitar apenas valores de 0 a 10
def validar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("valor invalido")
        except ValueError:
             print("valor invalido, digite apenas números.")

#validar matricula para usar função de busca e remoção no banco de dados
def validar_matricula(codigo):
    while True:
        try:
            digito = int(input(codigo))
            if digito > 0:
                return digito
            else:
                print("código invalido")
        except ValueError:
            print("valor invalido, digite apenas números.")

def validar_nome(aluno):
    return aluno.replace(" ","").isalpha()

def cadastrar_aluno():
    print("\n----------------NOVO CADASTRO-----------------")
    matricula = validar_matricula("matricula: ")
    while True:
        aluno = str(input("Digite o seu aluno: "))
        if validar_nome(aluno):
            break
        else:
            print("aluno invalido")
    nota1 = validar_nota("Digite a primeira nota: ")
    nota2 = validar_nota("Digite a segunda nota: ")
    media = calcular_media(nota1, nota2)
    situacao = verificar_situacao(media)

    return{"matricula":matricula,
            "aluno":aluno,
            "media":media,
            "situacao":situacao}

def exibit_lista(lista_aluno):
    print("-"*64)
    print("FICHA DA LISTA".center(64))
    print("-"*64)
    print(f"{'Matricula':<10} | {'Aluno':<30} | {'Media':<5} | {'Situacao':<5}")
    print("-"*64)
    for dados in lista_aluno:
        print(f"{dados['matricula']:<10} | {dados['aluno']:<30} | {dados['media']:<5} | {dados['situacao']:<5}")
        print('-'*64)

   #Operação do Menu

Lista = []

while True:
    operacao = str(input("Digite I (para iniciar) ou S (para sair): "))

    if operacao == "I" or operacao == "i":
        novo_Aluno = cadastrar_aluno()
        Lista.append(novo_Aluno)
        print("Cadastrado com sucesso! \n")

    elif operacao == "S" or operacao == "s":
        exibit_lista(Lista)
        break

    else:
        print("invalido")