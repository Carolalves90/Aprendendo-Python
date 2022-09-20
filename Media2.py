def lernotas():
    n = float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1,n2):
    media=(n1+n2)/2
    print("nota1: ", n1)
    print("nota2: ", n2)
    print("média: ", media, "Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a,b)