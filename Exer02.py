try:
    with open("frase.txt", "r") as arq:
        lerLinhas = arq.readline()
        
        linhasNaoVazias = [linha for linha in lerLinhas if linha.strip()]
        print("Linhas não vazias: ", len(linhasNaoVazias))
except PermissionError:
    print("Sem permissão para ler o arquivo frase.txt...")