import json
from datetime import datetime, timedelta


def gate_filters(response_text):
    datas = json.loads(response_text)
    
    # data de hoje
    today = datetime.today()
    # D + 4
    limit_day = today + timedelta(days=4)
    
    if datas.get("Result") != "OK":
        print("Ocorreu algum erro")
        return []
    
    records = datas.get("Records", [])

    results = []
    
    for r in records:
        gate_dry = r.get("AberturaGateDry")
        deadline = r.get("DeadlineCarga")
        agencia = r.get("Agencia")
        is_janeladry_open = r.get("JanelaDry") or ""
        gate_confirmado = r.get("QtdCategoriaEfetiva") > 0

        if not gate_dry or "0001" in gate_dry:
            continue

        date_gate = datetime.strptime(gate_dry.strip(), "%d/%m/%Y %H:%M:%S").date()
        date_deadline = datetime.strptime(deadline.strip(), "%d/%m/%Y %H:%M:%S").date()

        if (today.date() <= date_gate <= limit_day.date() or is_janeladry_open and today.date() <= date_deadline):
            results.append({
                "navio": r.get("Navio"),
                "agencia": agencia,
                "viagem": r.get("Viagem"),
                "data_gate": gate_dry,
                "deadline": deadline,
                "gateConfirmado": gate_confirmado,
                "janelaDry": is_janeladry_open
            })

    return sorted(results, key=lambda r: r['deadline'])