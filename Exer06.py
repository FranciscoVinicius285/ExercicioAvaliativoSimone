import string

try:
    with open("texto.txt", "r") as arq:
        lerLinhas = arq.read().lower()
        print("texto com todas palavras minúsculas: ",lerLinhas)

    for p in string.punctuation:
        aqrSemPontuacao = lerLinhas.replace(p, "")

    

    palavraDistintas = set(aqrSemPontuacao.split())

    print("A quantidade de palavras distintas: ",len(palavraDistintas))

except FileNotFoundError:
    print("Arquivo não encontrado")
