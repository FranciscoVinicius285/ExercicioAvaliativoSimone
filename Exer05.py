itensDocument = set()

for arquivo in["lista_a.txt", "lista_b.txt"]:
    try:
        with open(arquivo, "r") as arq:
            for linha in arq:
                itensDocument.add(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado")
    
    with open("lista_uniq.txt", "w") as arquivo:
        for itemUnicos in sorted(itensDocument):
            arquivo.write(itemUnicos + "\n")


print("Arquivo criado com sucesso!")
