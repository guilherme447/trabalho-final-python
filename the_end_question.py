import sys
from click import clear

clear()

lista_produtos = []


def manu ():
    clear()
    print ('\n \t Sua lista de produtos\n')
    print ('\t1 mostrar todos os items  da lista')
    print ('\t2 adicionar item à lista')
    print ('\t3 Remover item da lista ')
    print ('\t4 Apagar todos os itens da  lista')
    print ('\t5 gravar lista')
    print ('\t6 Gravar lista  versionada')
    print ('\t7 Carregar arquivo.txt na lista')
    print ('\t8 Sair')
    op = input('Opções: ')
    return op
    

def mostra_itens():
    clear()
    print ('todos itens da lista')
    if lista_produtos == []:
         print('\n*** Lista vazia ***\n')
    else:
        for i in lista_produtos:
            print(i)
    input('\n Enter para continuar!')

           

def add_item():
    clear()
    print ('\n \n \t Aqui voçê vai adicionar item')
    add = input('\n Adicionar um produto: ')
    lista_produtos.append(add)
    input('\n Enter para continuar!')

    


def remover_item():
    clear()
    print ('area para remover o item')
    if lista_produtos == []:
        print('\n*** Lista vazia ***\n')
    else:
        mostra_itens()  
        item_remover = input('Digite o nome do produto a ser removido: ')
        if item_remover in lista_produtos:
            lista_produtos.remove(item_remover)
            print(f'\nProduto "{item_remover}" removido com sucesso!\n')
        else:
            print(f'\nProduto "{item_remover}" não encontrado na lista.\n')
    input('Enter para continuar!')


def apagar_todos_itens():
     clear()
     lista_produtos.clear()  
     print('\nTodos os itens foram apagados da lista.\n')
     input('Enter para continuar!')



def gravar_lista():
    clear()
    print ('\n \t Aqui voçê vai gravar todos os itens da lista')
    if  lista_produtos == []:
        print('\n*** Lista vazia ***\n')        
    else:
         file =  open('produtos.txt', 'w')
         for i in lista_produtos:
             file.write(f'{i}\n')
         file.close()
    input('\n Enter para continuar!')   


def gravar_lista_versionada():
    clear()
    print ('\n \t Aqui vc vai adicionar uma lista nova')
    if  lista_produtos == []:
        print('\n*** Lista vazia ***\n')        
    else:
         file =  open('nova_lista.txt', 'w')
         for i in lista_produtos:
             file.write(f'{i}\n')
         file.close()
    input('\n Enter para continuar!') 



def carregar_arquivo_lista():
    clear()
    print ('\n \n ***aqui voçê vai pegar dados das lista anteriores***')
    lista_produtos = open('produtos.txt', 'r')
    for i in lista_produtos:
          lista_produtos.readline()
          print(i.strip())





###############################################   


while True:
    op = manu()
    if op == '1':
         mostra_itens()
    elif op == '2':
         add_item()
    elif op == '3':
         remover_item()
    elif op == '4':
         apagar_todos_itens()
    elif op == '5':
         gravar_lista()
    elif op == '6':
         gravar_lista_versionada()
    elif op == '7':
        carregar_arquivo_lista()
    elif op == '8':
         sys.exit()
    
         
    

        

    

    















       
    


    

