p=0
with open("livros_recomendados.txt","r") as recom:
    for linhas in recom:
        p+=1
        dados = linhas.strip().split(",")
        print(str(p)+"º lugar. Nota:"+str(dados[3])+str(dados[1])+", Escrito por:"+str(dados[2])+", Em: "+str(dados[0]))