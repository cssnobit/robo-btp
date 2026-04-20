from scraper import data_collect
from parser import gate_filters

if __name__ == "__main__":
    res = data_collect()

    if not res:
        print("Falha na coleta")
        exit()

    print(res[:2000])
    exit()

    gates = gate_filters(res)