from cadastro_clientes import db_clientes
import os

usr = input('DIGITE O NOME DO USUARIO:')
os.system('clear')
opcao = input('BEM-VINDO, ESCOLHA UMA DAS OPÇOES: \n1-CLIENTES\n  ')
if opcao == '1':
    clientes = input('ESCOLHA: \n1 cadastrar \n2-BUSCAR CLIENTE \n ')
    if clientes == '1':
        db_clientes.cadastro_clientes()
    elif clientes == '2':
        buscar_cpf = input('Digite o cpf:')
        db_clientes.buscar_db_cli(buscar_cpf)
