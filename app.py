from flask import Flask, redirect, render_template, request, url_for
from wtforms import Form, FormField

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/absorventes')
def absorventes():
    return render_template('absorventes.html')

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html', resultado_descartavel='conversao_carbono_descartavel', resultado_coletor='conversao_carbono_coletor')

total_absorvente = 0
conversao_carbono_coletor = 0
conversao_carbono_descartavel = 0

@app.route('/', methods=['GET', 'POST'])
def form_calculadora():
    if request.method == 'POST':
        qtdade = int(Form.qtdade_absorvente.data)
        dias = int(FormField.dias_absorvente.data)
        total_absorvente = qtdade * dias
        conversao_carbono_descartavel = (total_absorvente * 20.19) / 195
        conversao_carbono_coletor = total_absorvente * 1.77

    return render_template('resultado.html')