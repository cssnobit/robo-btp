import json
from config import TODAY, TOMORROW
from datetime import datetime

def gate_filters(response_text):
    datas = json.loads(response_text)
    
    if datas.get("Result") != "OK":
        print("Ocorreu algum erro")
        return []
    
    records = datas.get("Records", [])

    results = []

    for r in records:
        gate_dry = r.get("AberturaGateDry")
        deadline = r.get("DeadlineCarga")
        agencia = r.get("Agencia")

        if not gate_dry or "0001" in gate_dry:
            continue

        date_gate = datetime.strptime(gate_dry.strip(), "%d/%m/%Y %H:%M:%S").date()

        if TODAY.date() <= date_gate <= TOMORROW.date():
            results.append({
                "navio": r.get("Navio"),
                "agencia": agencia,
                "viagem": r.get("Viagem"),
                "data_gate": gate_dry,
                "deadline": deadline
            })

    return results