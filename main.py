from scraper import data_colect
from parser import gate_filters

if __name__ == "__main__":
    res = data_colect()

    if not res:
        print("Falha na coleta")
        exit()

    gates = gate_filters(res)

    print("\nABERTURA(S) DE GATE:\n")

    for g in gates:
        print(g)