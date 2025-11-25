def valnota(n):
    loop = True
    while loop:
        try:
            n = float(input("Nota para o livro" +str(dados[1])+ " de "+str(dados[0])+ " Escrito por"+str(dados[2])+": "))
            if n > 10 or n < 0:
                raise NotaInvalida
            else:
                    loop = False
                    return n
        except (ValueError, NotaInvalida):
            print("NOTA INVÁLIDA!")
def valstatus(s):
    loop = True
    while loop:
        try:
            s = input("Status de leitura do livro" +str(dados[1])+ " de "+str(dados[0])+ " Escrito por"+str(dados[2])+" (Lido/Lendo/Na fila): ").capitalize()
            if s != "Lido" and s != "Lendo" and s != "Na fila":
                raise RespostaInvalida
            else:
                loop = False
                return s
        except (ValueError, RespostaInvalida):
            print("RESPOSTA INVÁLIDA!")
            
class NotaInvalida(Exception):
    pass
class RespostaInvalida(Exception):
    pass
n = s = None
with open("livros.txt","r") as livros:
    with open("livros_avaliacao.txt","w") as notas:
        for linhas in livros:
            dados = linhas.strip().split(",")
            n = valnota(n)
            s = valstatus(s)
            notas.write(f"{dados[0]}, {dados[1]}, {dados[2]}, {n}, {s}\n")
