with open("livros_avaliacao.txt","r") as aval:
    with open("livros_recomendados.txt","w") as recom:
        for linhas in aval:
            dados = linhas.strip().split(",")
            