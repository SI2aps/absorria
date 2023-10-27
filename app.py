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
comparacao_descartavel = 0 

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    form = ReusableForm(request.form)
    total_absorvente = 0
    conversao_carbono_coletor = 0
    conversao_carbono_descartavel = 0
    comparacao_descartavel = 0 

    if request.method == 'POST' and form.validate():
        qtdade = int(form.qtdade_absorvente.data)
        dias = int(form.dias_absorvente.data)
        total_absorvente = qtdade * dias
        conversao_carbono_descartavel = (total_absorvente * 20.19) / 195
        conversao_carbono_coletor = total_absorvente * 1.77
        comparacao_descartavel = (total_absorvente * 100) / 73428

    return render_template('calculadora.html',
                           total_absorvente=total_absorvente,
                           conversao_carbono_descartavel=conversao_carbono_descartavel,
                           conversao_carbono_coletor=conversao_carbono_coletor,
                           comparacao_descartavel=comparacao_descartavel,
                           form=form)

if __name__ == "__main__":
    app.run(debug=True)