from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['get'])
def hello_world():
    return render_template('index.html')

@app.route('/estoque', methods=['post'])
def estoque():
    nomeItem = request.form.get('nomeItem')
    desc = request.form.get('desc')
    genero = request.form.get('genero')
    autor = request.form.get('autor')
    quantidade = request.form.get('quantidade')
    precunit = request.form.get('precunit')

    #DICIONARIO DO ITEM ATUAL
    dici = {
        'nomeItem':nomeItem,
        'desc':desc,
        'genero':genero,
        'autor':autor,
        'quantidade':quantidade,
        'precunit':precunit,
    }
    arq = open('estoque.json', mode='r')
    dados = json.load(arq)
    dados = [d for d in dados]
    dados.append(dici)
    arq.close()
    arq = open('estoque.json', mode='w')
    arq.write(json.dumps(dados))
    return render_template('cadastro.html')

@app.route('/listagem', methods=['GET'])
def listagem():
    arq_estoque = open('estoque.json', mode='r')
    estoque = json.load(arq_estoque)
    return render_template('listagem.html', estoque=estoque)
if __name__ == '__main__':
    app.run()
