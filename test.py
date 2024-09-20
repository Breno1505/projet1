banco = [
{
        'codigo': 1,
        'titulo': 'Código limpo',
        'autor': 'Roberth',
        'categoria': 'Programação',
        'alugado': True,
        'preco': 15.90 
}
]
codigoAtual = 1 #variavel global

def addLivro(titulo:str, autor:str, categoria:str, preco:float):
    global codigoAtual
    codigoAtual += 1
    livro = {
       'codigo': 1,
        'titulo': codigoAtual,
        'autor': titulo,
        'categoria': autor,
        'alugado': False,
        'preco': preco 
    }
    banco.append(livro)
    print('livro cadastrado com sucesso')

def inputAddlivro():
   titulo = input('digite o titulo do livro:')
   autor = input('digite o autor do livro: ')
   categoria = input('digite a categoria do livro: ')
   preco = float(input('digite o preço do livro:'))
   addLivro(titulo,autor,categoria,preco)

def buscarporcodigo(codigo:int):
    for livro in banco:
        if livro['codigo'] == codigo:
            return livro
    return None

print(buscarporcodigo(1))
print(buscarporcodigo(2))

def editlivro(codigo:int, titulo: str,autor:str, categoria: str, preco: float):
    livro = buscarporcodigo(codigo)
    livro['titilo'] = titulo
    livro['autor'] = autor
    livro['categoria'] = categoria
    livro['preco'] = preco
    print('Dados alterados com sucesso!!')

def inputeditlivro():
    codigo = int(input('Digite o código do livro: '))
    if buscarporcodigo(codigo):
        titulo = input('digite o titulo: ')
        autor = input('digite o autor: ')
        categoria = input('digite a categoria: ')
        preco = float(input('digite o preço do livro: '))
        editlivro(codigo, titulo, autor, categoria, preco)
    else:
        print('Livro não encontrado!!')    

def inputbuscarporcodigo():
    codigo = int(input('digite o codigo do livro:'))
    livro = buscarporcodigo(codigo)
    if livro:
        print('---DADOS DO LIVRO---')
        print(f"codigo:{livro['codigo']}")
        print(f"titulo: {livro['titulo']}")
        print(f"autor: {livro['autor']}")
        print(f"categoria: {livro['categoria']}") 
        print(f"preço: {livro['preco']}")
        print(f"alugado: {livro['alugado']}")
        return
    print('livro não encontrado!!')      

def deletlivro(codigo: int):
    livro = buscarporcodigo(codigo)
    banco.remove(livro)
    print('livro removido com sucesso!')

def inputdeletelivro():
    codigo = int(input('digite o código do livro: '))
    livro = buscarporcodigo(codigo)
    if livro:
        deletlivro(codigo)
    else:
        print('livro não encontrado')    

def listarLivros():
    for livro in banco:
        print('---DADOS DO LIVRO---')
        print(f"codigo:{livro['codigo']}")
        print(f"titulo: {livro['titulo']}")
        print(f"autor: {livro['autor']}")
        print(f"categoria: {livro['categoria']}") 
        print(f"preço: {livro['preco']}")
        print(f"alugado: {livro['alugado']}")
        print('-'*50)

def alugarlivro(codigo:  int):
    livro = buscarporcodigo(codigo)
    livro['alugado'] = False

    print('alugado com sucesso')

def inputalugarlivro():
    codigo = int(input('digite o código do livro: '))
    livro = buscarporcodigo(codigo)
    if livro:
        alugarlivro(codigo)

def devolverlivro(codigo:  int):
    livro = buscarporcodigo(codigo)
    livro['alugado'] = False

    print('devolvido com sucesso')

def inputdevolverlivro():
    codigo = int(input('digite o código do livro: '))
    livro = buscarporcodigo(codigo)
    if livro:
        devolverlivro(codigo)



def menu():
    while True:
        print('--- BEM VINDO AO MENU ---')
        print('1 - Cadastrar livro')
        print('2 - Editar livro')
        print('3 - Buscar livro')
        print('4 - Remover livro')
        print('5 - Listar todos')
        print('6 - Alugar livro')
        print('7 - Devolver livro')
        opcao = input('Selecione uma opção:')
        if opcao == '1':
            inputAddlivro()
        elif opcao == '2':
            inputeditlivro()
        elif opcao == '3':
            inputbuscarporcodigo()    
        elif opcao == '4':
            inputdeletelivro()    
        elif opcao == '5':
            listarLivros()    
        elif opcao == '6':
            inputalugarlivro()
        elif opcao == '7':
            inputdevolverlivro()        
        else:
            break    
menu()