with open("livros.txt","r") as livros:
    for linhas in livros:
        dados = linhas.strip().split(",")
        print(dados)