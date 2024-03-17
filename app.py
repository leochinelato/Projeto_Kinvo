from flask import Flask, render_template, url_for, redirect, request, flash, session


class Stock:
    def __init__(self, name, amount):
        self.name = name
        self.amout = amount


stocks = []

app = Flask(__name__)
app.secret_key = '09UD A_DS09Sj)(i*&&)'


@app.route('/')
def index():
    return render_template('index.html', titulo='Portfolio', stocks=stocks)


@app.route('/new')
def novo():
    return render_template('new.html', titulo='New Stock')


@app.route(
    '/criar',
    methods=[
        'POST',
    ],
)
def criar():
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    alimento = Alimento(nome, quantidade)
    alimentos.append(alimento)
    return redirect(url_for('index'))


app.run(debug=True)
