import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='produtos',
)
cursor = conexao.cursor()


def create(nome_produto, valor):
    produto_nome = nome_produto
    valor_produto = valor
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{produto_nome}", {valor_produto})'
    cursor.execute(comando)
    conexao.commit()

def read():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    return print(resultado)

    
def update(nome_produto, valor):
    produto_nome = nome_produto
    valor_produto = valor
    comando = f'UPDATE vendas SET valor = {valor_produto} WHERE nome_produto = "{nome_produto}" '
    cursor.execute(comando)
    conexao.commit() 
 
def delete(nome_produto):
    produto_nome = nome_produto
    comando = f'DELETE FROM vendas WHERE nome_produto = "{produto_nome}"'
    cursor.execute(comando)
    conexao.commit() 

navegador = ""
print("ESTOQUE DE PRODUTOS\n")
print("O que deseja?\n1 - Verificar Produtos\n2 - Adicionar Produtos\n3 - Atualizar Produto\n4 - Apagar produto.   \nDigite 0 Para Sair")
while navegador != 0:
    navegador = int(input("Navegador:"))
    if(navegador == 0):  #Sair do navegador
        break
    elif(navegador == 1): #visualizar produtos cadastrados
        read()
    elif(navegador == 2): # adicionar produtos no estoque
        nome_produto = input("Nome do Produto:")
        valor = int(input("Valor:"))
        create(nome_produto, valor)
        read()
    elif(navegador == 3): #atualizar valor do produto
        nome_produto = input("Nome do Produto:")
        valor = int(input("Valor:"))
        update(nome_produto, valor)
        read()
    elif(navegador == 4): #remover produto do estoque
        read()
        nome_produto = input("Nome do Produto:")
        delete(nome_produto) 
        read()
    else:
        print("Ocorreu um erro")


cursor.close()
conexao.close()