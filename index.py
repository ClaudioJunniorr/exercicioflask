from flask import Flask
# criando o objeto
aplicativo=Flask(__name__)
@aplicativo.route('/')
def index():
    return 'Estilo do Rei Barbearia'
@aplicativo.route('/login.html')
def login():
    return 'Login funciona'
@aplicativo.route('/novoagentamento.html')
def novoAgendamento():
    return ' Novo agendamento'
@aplicativo.route('/novocliente.html')
def novocliente():
    return ' cliente novo na área'
@aplicativo.route('/novofuncionario.html')
def novofuncionario():
    return ' funcionario novo na area '
@aplicativo.route('/novoservico.html')
def novoservico():
    return ' servico em funcionamento '
@aplicativo.route('/logout.html')
def logout():
    return ' Saiu da tela'
aplicativo.run(debug=True)