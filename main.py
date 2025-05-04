import sys
import time
import csv
import json
from automato import AutomatoFinito

def carregar_automato(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def carregar_testes(caminho):
    testes = []
    with open(caminho, 'r', encoding='utf-8') as f:
        leitor = csv.reader(f, delimiter=';')
        for linha in leitor:
            palavra, esperado = linha
            testes.append((palavra, int(esperado)))
    return testes

def salvar_resultados(caminho, resultados):
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        for linha in resultados:
            escritor.writerow(linha)

def main():
    if len(sys.argv) != 4:
        print("Uso: python main.py arquivo_automato.aut arquivo_testes.in arquivo_saida.out")
        sys.exit(1)

    arq_automato = sys.argv[1]
    arq_testes = sys.argv[2]
    arq_saida = sys.argv[3]

    automato = AutomatoFinito(carregar_automato(arq_automato))
    testes = carregar_testes(arq_testes)

    resultados = []
    for palavra, esperado in testes:
        inicio = time.perf_counter()
        aceito = automato.aceita(palavra)
        fim = time.perf_counter()
        tempo = round(fim - inicio, 6)
        resultados.append([palavra, esperado, int(aceito), tempo])

    salvar_resultados(arq_saida, resultados)

if __name__ == "__main__":
    main()