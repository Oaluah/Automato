import json
from collections import defaultdict, deque

class AutomatoFinito:
    def __init__(self, config):
        self.estado_inicial = config["initial"]
        self.estados_finais = set(config["final"])
        self.transicoes = defaultdict(list)

        for t in config["transitions"]:
            origem = t["from"]
            simbolo = t["read"]
            destino = t["to"]
            self.transicoes[(origem, simbolo)].append(destino)

    def epsilon_closure(self, estados):
        fechamento = set(estados)
        fila = deque(estados)

        while fila:
            estado = fila.popleft()
            for destino in self.transicoes.get((estado, None), []):
                if destino not in fechamento:
                    fechamento.add(destino)
                    fila.append(destino)

        return fechamento

    def aceita(self, palavra):
        estados_atuais = self.epsilon_closure([self.estado_inicial])

        for simbolo in palavra:
            proximos = set()
            for estado in estados_atuais:
                destinos = self.transicoes.get((estado, simbolo), [])
                for destino in destinos:
                    proximos.update(self.epsilon_closure([destino]))
            estados_atuais = proximos

        return any(estado in self.estados_finais for estado in estados_atuais)