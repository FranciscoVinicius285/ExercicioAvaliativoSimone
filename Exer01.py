try:
    with open("notas.txt", "r") as arq:
        ler = arq.read()
except FileNotFoundError:
    with open("notas.txt", "w") as arq:
        arq.write("Arquivo criado!")
    with open("notas.txt", "r") as arq:
        ler = arq.read()