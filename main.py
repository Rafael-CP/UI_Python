from tkinter import *

def botao():
    x['text'] = 'botao pressionado'
    x['fg'] = 'red'

#configuracoes inicias
janela = Tk()
janela.title('Janela')  #titulo da janela
janela.geometry('800x600') #tamanho da janela ao ser aberta (largura x altura)
janela.resizable(False,False) #impede a janela de ser redimensionada pelo usuario

#Label(janela, text='Hello', bg='pink1', fg='white', padx=10, pady = 10).grid(row=0, column=0) #cria uma caixa de texto
#             texto exibido - cor do fundo - cor da fonte - espaçamento entre o texto

#Entry(janela, bg='orange', fg='blue', show='*').grid(row=0, column=1) # Abre uma caixa de texto para entrada de dados
#             cor do fundo - cor da fonte - troca caractere mostrado

Button(janela, text='pressione',bg='gray', fg='black', height=10, width=20, command=botao).grid(row=0, column=2) #Cria um botão interativo na janela
#             texto exibido - cor do fundo - cor da fonte - espaçamento entre o botao - comando a ser executado (sem parenteses na funcao)

x = Label(janela, text='pressione o botao', fg='black')
x.grid(row=1, column=2)

#cria e abre um loop da janela
janela.mainloop()
