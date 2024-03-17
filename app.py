from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
)


class Stock:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


stocks = []

app = Flask(__name__)
app.secret_key = '09UD A_DS09Sj)(i*&&)'


@app.route('/')
def index():
    return render_template('index.html', title='Portfolio', stocks=stocks)


@app.route('/new')
def new():
    return render_template('new.html', title='New Stock')


@app.route(
    '/create',
    methods=[
        'POST',
    ],
)
def create():
    name = request.form['name']
    amount = request.form['amount']
    stock = Stock(name, amount)
    stocks.append(stock)
    return redirect(url_for('index'))


app.run(debug=True)
