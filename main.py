from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios para simular o conteúdo
PRODUTOS = [
    {"id": 1, "nome": "Caderno SHED", "preco": "R$ 25,00", "cat": "Papelaria"},
    {"id": 2, "nome": "Caneta Premium", "preco": "R$ 12,00", "cat": "Papelaria"},
]

@app.route('/')
def home():
    return render_template('index.html', titulo="Página Principal")

@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html', titulo="Meus Favoritos")

@app.route('/categoria/<nome>')
def categoria(nome):
    return render_template('categoria.html', titulo=f"Categoria: {nome}", categoria=nome)

@app.route('/cesto')
def cesto():
    return render_template('cesto.html', titulo="Meu Cesto")

if __name__ == '__main__':
    app.run(debug=True)
