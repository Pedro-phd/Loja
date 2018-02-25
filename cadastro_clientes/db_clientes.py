import sqlite3
connection = sqlite3.connect('db_clientes.db')
c = connection.cursor()
def cadastro_clientes():

    print('TODOS OS DADOS DEVERAM SER INSERIDOS COM LETRA MINUSCULA E SEM PONTUAÇÃO!!!')
    nome = input('DIGITE O NOME DO CLIENTE: ')
    rua = input('DIGITE O ENDEREÇO DO CLIENTE: ')
    numero = int(input('DIGITE O NUMERO DE CONTATO DO CLIENTE: '))
    cpf = int(input('DIGITE O CPF DO CLIENTE: '))

    def criar_db_cli():
        c.execute('CREATE TABLE IF NOT EXISTS db_clientes (nome text, rua text, numero integer, cpf integer)')
    def preencher_db():
        c.execute('INSERT INTO db_clientes VALUES (?, ?, ?, ?)',(nome, rua, numero, cpf))
    criar_db_cli()
    preencher_db()
    connection.commit()


def buscar_db_cli(bus_cpf):
    sql = 'SELECT * FROM db_clientes WHERE cpf = ?'
    for row in c.execute(sql, [bus_cpf]):
        print(row)
