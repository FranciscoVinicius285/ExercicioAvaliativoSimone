try:
    try:
        with open("comentarios.txt", 'r', encoding="utf-8") as arquivo:
            conteudoArq = arquivo.read()
    except UnicodeDecodeError:
        with open("comentarios.txt", 'r', encoding="latin-1") as arquivo:
            conteudoArq = arquivo.read()

    textoLimpo = conteudoArq.replace("  "," ").replace("...",".")

    with open("comentarios_limpos.txt", "w") as arq:
        arq.write(textoLimpo)
        print("Arquivo criado e limpo")

except FileNotFoundError:
    print("Arquivo não encontrado: comentarios.txt")
