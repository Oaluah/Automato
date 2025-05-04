# Simulador de Autômatos Finitos

Este projeto é uma ferramenta de linha de comando para simulação de autômatos finitos, incluindo:
- Autômatos Determinísticos (AFD)
- Autômatos Não Determinísticos (AFN)
- AFNs com transições vazias (ε-moves)

## Como usar

```bash
python main.py exemplo.aut exemplo.in exemplo.out
```

### Formato dos arquivos

**JSON do autômato (`.aut`)**

```json
{
  "initial": 0,
  "final": [4],
  "transitions": [
    {"from": 0, "read": "a", "to": 1},
    {"from": 1, "read": "b", "to": 2},
    {"from": 2, "read": null, "to": 4}
  ]
}
```

**CSV de testes (`.in`)**

```
ab;1
aab;0
abc;0
```

**Saída gerada (`.out`)**

```
ab;1;1;0.000032
aab;0;0;0.000024
abc;0;0;0.000027
```