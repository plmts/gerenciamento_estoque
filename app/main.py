from flask import Flask, request, jsonify
from database import engine, SessionLocal, Base
from models import Produto

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

@app.route("/produtos", methods=["POST"])
def post_produto():
    session = SessionLocal()
    data = request.json
    produto = Produto(nome=data['nome'], valor=data['valor'], marca=data['marca'], descricao=data['descricao'], quantidade=data['quantidade'])
    session.add(produto)
    session.commit()
    session.refresh(produto)
    session.close()

    return jsonify(produto.to_dict()), 201

@app.route("/produtos", methods=["GET"])
def get_produtos():
    session = SessionLocal()
    produtos = session.query(Produto).all()
    result = [produtos.to_dict() for produto in produtos]
    session.close()
    return jsonify(result)

@app.route("/produtos/<int:produto_id>", methods=["GET"])
def get_produto(produto_id):
    session = SessionLocal()
    produto = session.query(Produto).get(produto_id)
    session.close()
    if produto:
        return jsonify(produto.to_dict())
    return jsonify({"ERRO": "Produto não encontrado"}), 404

@app.route("/produtos/<int:produto_id>", methods=['PUT'])
def put_produto(produto_id):
    session = SessionLocal()
    produto = session.query(Produto).get(produto_id)

    if not produto:
        session.close()
        return jsonify({"ERRO": "Produto não encontrado"}), 404
    
    data = request.json
    produto.nome = data.get("nome", produto.nome)
    produto.valor = data.get("valor", produto.valor)
    produto.marca = data.get("marca", produto.marca)
    produto.descricao = data.get("descricao", produto.descricao)
    produto.quantidade = data.get("quantidade", produto.quantidade)

    session.commit()
    session.refresh(produto)
    session.close()
    return jsonify(produto.to_dict())

@app.route("/produtos/<int:produto_id>", methods=['DELETE'])
def excluir_produto(produto_id):
    session = SessionLocal()
    produto = session.query(Produto).get(produto_id)
    if not produto:
        session.close()
        return jsonify({"ERRO": "Produto não encontrado"}), 404
    
    session.delete(produto)
    session.commit()
    session.close()
    return jsonify({"Mensagem": "O produto foi deletado"})


# Rotas
@app.route("/")
def home():
    return {"testando": "123"}



if __name__ == "__main__":
    app.run(debug=True)