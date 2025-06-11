from bottle import run, Bottle, request, template

app = Bottle()


@app.route('/login')
def index():
    return template('login')

def check_login(nome, senha):
    print(f'Nome: {nome}, Senha: {senha}')
    return True

@app.route('/login', method='POST')
def acao_login():
    nome = request.forms.get('nome')
    senha = request.forms.get('senha')

    if check_login(nome, senha):
        return f'<html><body align="center"><h1>Login realizado com sucesso!</h1></body></html>'
    else:
        return f'<html><body align="center"><h1>Login falhou!</h1></body></html>'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    run(app,host='localhost', port=8080, debug=True, reloader=True)