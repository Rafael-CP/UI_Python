from tkinter import *
from tkinter import ttk


arv = Tk()
arv.title('Tree View')

tree = ttk.Treeview(arv, selectmode = 'browse', column = ('column1', 'column2', 'column3', 'column4'), show = 'headings')
#            pai da tree - modo de exibicao - colunas que tera na tree, devem ser declaradas antes - como sera exibido

tree.column('column1',width = 200, minwidth = 50, stretch = NO)
#                     ^Tamanho inicial ^tamanho mínimo
tree.heading('#1', text = 'Nome')
#             ^Hashtag indica a ordem que elas ficarão dispostas
tree.column('column2',width = 60, minwidth = 40, stretch = NO)
tree.heading('#2', text = 'Idade')
#                    ^Título da coluna
tree.column('column3',width = 120, minwidth = 40, stretch = NO)
tree.heading('#3', text = 'CPF')

tree.column('column4',width = 200, minwidth = 60, stretch = NO)
tree.heading('#4', text = 'Endereço')

elemento = ['Rafael', 21, '11699783632', 'Brasil']
elemento2 = ['Leafar', 15, '2132342344', 'Russia']
#deve-se criar uma array com os elementos que devem ser inseridos na lista
tree.insert("", END, values = elemento, tag = '1')
tree.insert("", END, values = elemento2, tag = '1')


tree.grid(row = 0, column = 0)

arv.mainloop()