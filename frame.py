from tkinter import *

janela = Tk()
janela.title("Teste de frame")
janela.geometry("800x600")

frame = Frame(janela, width = 300, height = 300, bg = 'red').grid(row = 0, column = 0)
#frames servem para caso queira colocar labels e butoes dentro de uma area especifica
#assim deve se declarar o frame como pai no inicio dos parametros, por exemplo

Label(frame, text = 'lsdakçasd').grid(row = 0, column = 0)

janela.mainloop()