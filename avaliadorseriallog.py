import os
import time
from multiprocessing import Process, Manager, cpu_count

def consolidar_resultados(resultados):
    total_linhas = 0
    total_palavras = 0
    total_caracteres = 0
    contagem_global = {"erro": 0, "warning": 0, "info": 0}
    for r in resultados:
        total_linhas += r["linhas"]
        total_palavras += r["palavras"]
        total_caracteres += r["caracteres"]
        for chave in contagem_global:
            contagem_global[chave] += r["contagem"][chave]
    return {"linhas": total_linhas, "palavras": total_palavras, "caracteres": total_caracteres, "contagem": contagem_global}

def processar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.readlines()
    total_linhas = len(conteudo)
    total_palavras = 0
    total_caracteres = 0
    contagem = {"erro": 0, "warning": 0, "info": 0}
    for linha in conteudo:
        palavras = linha.split()
        total_palavras += len(palavras)
        total_caracteres += len(linha)
        for p in palavras:
            if p in contagem:
                contagem[p] += 1
        for _ in range(1000):
            pass
    return {"linhas": total_linhas, "palavras": total_palavras, "caracteres": total_caracteres, "contagem": contagem}

def produtor(pasta, fila, n_consumidores):
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(".txt"):
            caminho = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho):
                fila.put(caminho)
    for _ in range(n_consumidores):
        fila.put(None)

def consumidor(fila, fila_resultados):
    resultados_locais = []
    while True:
        arquivo = fila.get()
        if arquivo is None:
            break
        resultados_locais.append(processar_arquivo(arquivo))
    fila_resultados.put(resultados_locais)

def executar_paralelo(pasta, n_processos):
    print(f"\n=== INÍCIO DA EXECUÇÃO COM {n_processos} PROCESSOS ===")
    with Manager() as manager:
        fila = manager.Queue()
        fila_resultados = manager.Queue()
        processos = []

        inicio = time.time()
        p_produtor = Process(target=produtor, args=(pasta, fila, n_processos))
        p_produtor.start()

        for _ in range(n_processos):
            p = Process(target=consumidor, args=(fila, fila_resultados))
            p.start()
            processos.append(p)

        p_produtor.join()
        for p in processos:
            p.join()

        resultados = []
        while not fila_resultados.empty():
            resultados.extend(fila_resultados.get())

        fim = time.time()
        resumo = consolidar_resultados(resultados)

        print(f"=== FIM DA EXECUÇÃO COM {n_processos} PROCESSOS ===")
        print(f"Arquivos processados: {len(resultados)}")
        print(f"Tempo total: {fim - inicio:.4f} segundos")
        print("=== RESULTADO CONSOLIDADO ===")
        print(f"Total de linhas: {resumo['linhas']}")
        print(f"Total de palavras: {resumo['palavras']}")
        print(f"Total de caracteres: {resumo['caracteres']}")
        print("Contagem de palavras-chave:")
        for k, v in resumo["contagem"].items():
            print(f"  {k}: {v}")
        return fim - inicio

if __name__ == "__main__":
    pasta = os.path.join(os.path.dirname(__file__), "log2")
    processos_testados = [1, 2, 4, 8, 12]
    for n in processos_testados:
        n = min(n, cpu_count())
        executar_paralelo(pasta, n)
