

with open("livros.txt","r") as livros:
    with open("livros_avaliacao.txt","w") as notas:
        for linhas in livros:
            dados = linhas.strip().split(",")
        try:
            n = float(input("Nota para o livro" +str(dados[1])+ " de "+str(dados[0])+ " Escrito por"+str(dados[2])+": "))
            s = input("Status de leitura do livro" +str(dados[1])+ " de "+str(dados[0])+ " Escrito por"+str(dados[2])+" (Lido/Lendo/Na fila): ")
            notas.write(f"{n}, {s}\n")
        except:
           
              
