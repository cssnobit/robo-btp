from flask import Flask, jsonify, render_template
from parser import gate_filters
from scraper import data_collect
from datetime import datetime, timedelta
import time
import threading

app = Flask(__name__)

cache = {
    "datas": [],
    "last_update": None,
    "next_update": None
}


def is_gate_confirmado(datas):
    for g in datas:
        if g.get("gateConfirmado") and g.get("janelaDry") != "SIM":
            return True

    return False

def update_cache():
    while True:
        try:
            response = data_collect()
            filtered = gate_filters(response)

            now = datetime.now()

            cache["datas"] = filtered

            if is_gate_confirmado(filtered):
                interval = 180
            else:
                interval = 900

            cache["last_update"] = now
            cache["next_update"] = now + timedelta(minutes=interval/60)

        except Exception as e:
            print("Erro ao atualizar cache:", e)
            interval = 300

        time.sleep(interval)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gates")
def gates():
    if not cache["datas"]:
        return jsonify({
            "datas": [],
            "last_update": None,
            "next_update": None
        })

    return jsonify({
        "datas": cache["datas"],
        "last_update": cache["last_update"].strftime("%d/%m/%Y %H:%M:%S") if cache["last_update"] else None,
        "next_update": cache["next_update"].strftime("%d/%m/%Y %H:%M:%S") if cache["next_update"] else None
    })


threading.Thread(target=update_cache, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
