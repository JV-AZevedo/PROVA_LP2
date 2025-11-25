e = []
with open("livros_recomendados.txt","w") as recom:
    for i in range(5):
        m = -1
        with open("livros_avaliacao.txt","r") as aval:
            for linhas in aval:
                dados = linhas.strip().split(",")
                if dados[0] in e:
                    continue
                elif "Na fila" in dados[4]:
                    continue
                elif float(dados[3]) > m:
                    m = float(dados[3])
                    l = []
                    l.append(dados[0])
                    l.append(dados[1])
                    l.append(dados[2])
                    l.append(dados[3])
                    l.append(dados[4])
            e.append(l[0])
            recom.write(f"{l[0]}, {l[1]}, {l[2]}, {l[3]}, {l[4]}\n")