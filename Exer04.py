jogadores = {}
for linha in open("jogadores_times.txt"):
    try:
        nome, time = linha.strip().split(",",1)
        jogadores[nome.strip()] = time.strip()
    except:
        open("linhas_invalidas.log", "a").write(linha)

print(jogadores)