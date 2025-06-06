from flask import Flask, jsonify, request

app = Flask(__name__)

Produtos = [
    {"id": 1, "Produto": "Computador ryzen 5, 500gb, 16gb ram"},
    {"id": 2, "Produto": "Smart tv 4k 75' + Alexa"},
    {"id": 3, "Produto": "Playstation 5 midia digital + 3 jogos"},
    {"id": 4, "Produto": "Iphone 16 green 500gb"},
    {"id": 5, "Produto": "Samsung galaxy S25 ultra 1TB"}
]

@app.route('/Produtos', methods=['GET'])
def get_Produtos():
    return jsonify(Produtos)

@app.route('/Produtos', methods=['POST'])
def adicionar_Produto():
    nova_Produto = request.get_json()
    if not nova_Produto or 'Produto' not in nova_Produto:
        return jsonify({"erro": "Dados inválidos"}), 400

    novo_id = Produtos[-1]['id'] + 1 if Produtos else 1
    Produto_completa = {"id": novo_id, "Produto": nova_Produto['Produto']}
    Produtos.append(Produto_completa)
    return jsonify(Produto_completa), 201

if __name__ == '__main__':
    app.run(debug=True)
