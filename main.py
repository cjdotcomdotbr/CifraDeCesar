#Cifra de cesar
#17.03.2018
#Gabriel Henrique Silva

from tkinter import *

janela = Tk()
def bt1_cifrar():
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    cript = list(et1.get())
    salto = int(et2.get())
    cont = 0
    cifra = []
    lista = []

    while cont < salto:
        cont += 1
        alfabeto.insert(0, 0)
    for i in range(len(cript)):
        for j in range(len(alfabeto)):
            if cript[i] == alfabeto[j]:
                lista.append(j)

    while cont != 0:
        cont -= 1
        alfabeto.remove(0)
    for n in range(len(lista)):
        for m in range(len(alfabeto)):
            if lista[n] > 25:
                lista[n] -= 25
            elif lista[n] == m:
                cifra.append(alfabeto[m])

    lb1['text'] = '-'.join(cifra).upper()

#Onde é mostrado a cifra informada, o programa não decifra...
def bt2_decifrar():
    cifra = str(et1.get())
    lb1['text'] = '-'.join(cifra)

def sair():
    janela.destroy()
    quit()

janela.geometry('300x400+300+100')
janela['bg'] = 'blue'
janela.title('Cifra de Cesar')

#Entrada de dados
et1 = Entry(janela)
et1.place(x=10, y=10, width='280', height='100')
et2 = Entry(janela)
et2.place(x=10, y=131, width='280')

#Botões(cifrar, decifrar, sair)
bt1 = Button(janela, text='Criptografar', width='10', command=bt1_cifrar)
bt1.place(x=10, y=170)
bt2 = Button(janela, text='Descifrar', width='10', command=bt2_decifrar)
bt2.place(x=10, y=317)
bt3 = Button(janela, text='Sair', command=sair, width='10')
bt3.place(x=205, y=360)

#Local da resposta e indicatorio de inteiro para o salto de letras
lb1 = Label(janela, text='...', width='39', height='5')
lb1.place(x=10, y=217)
lb2 = Label(janela, text='Salto')
lb2.place(x=20, y=110)
lb2['bg'] = 'blue'

janela.mainloop()
