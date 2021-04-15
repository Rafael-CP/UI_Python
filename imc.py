from tkinter import *

def calculo():
    pesoC = float(peso.get())
    alturaC = float(altura.get())
    resposta['text'] = f'Seu IMC é {pesoC/(alturaC**2):.2f} !'

imc = Tk()
imc.title('Cálculo de IMC')  #titulo da janela
imc.geometry('400x100') #tamanho da janela ao ser aberta (largura x altura)
imc.resizable(False, False) #impede a janela de ser redimensionada pelo usuario

Label(imc, text = 'Insira seu peso (Kilogramas): ', fg = 'black').grid(row = 0, column = 0)
peso = Entry(imc)
peso.grid(row = 0, column = 1)

Label(imc, text = 'Insira sua altura (Metros): ', fg = 'black').grid(row = 1, column = 0)
altura = Entry(imc)
altura.grid(row = 1, column = 1)

Button(imc, text = 'Calcular IMC', padx = 10, pady = 10, command = calculo).grid(row = 0, column = 2, rowspan = 2)

resposta = Label(imc, text='')
resposta.grid(row=2, column=1)

imc.mainloop()