from flask import Flask, request, jsonify
from fisica import simular_voo
from rede_neural import prever_estabilidade

app = Flask(__name__)

@app.route('/simular', methods=['POST'])
def simular():
    params = request.get_json()
    resultados = simular_voo(params)
    estabilidade = prever_estabilidade(params)
    resultados['estabilidade'] = estabilidade
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
