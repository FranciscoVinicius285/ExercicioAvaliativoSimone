itens = set()

for arquivo in["lista_a.txt", "lista_b.txt"]:
    try:
        with open (arquivo, "r") as arq:
            for linha in arq:
                itens.add(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado")

    with open("lista_unica.txt", "w") as arquivo:
        for item in sorted(itens):
            arquivo.write(item + "\n")
    print("Arquivo criado")