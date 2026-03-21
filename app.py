from flask import Flask, jsonify, render_template
from parser import gate_filters
from scraper import data_colect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gates")
def gates():
    resp = data_colect()

    if not resp:
        return jsonify([])

    datas = gate_filters(resp)

    return jsonify(datas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
