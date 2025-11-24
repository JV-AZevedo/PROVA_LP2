with open("livros.txt","r") as livros:
    with open("livros_avaliacao.txt","w"):
        for linhas in livros:
            dados = linhas.strip().split(",")
            n = float(input("Nota para o livro " +str(dados[1])+ " de "+str(dados[0])+ " Escrito por"+str(dados[2])+": "))
              
