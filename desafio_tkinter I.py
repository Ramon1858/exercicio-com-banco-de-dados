import sqlite3 #banco dados    
import tkinter as tk #interface
from tkinter import messagebox#caixa de mensagem
from tkinter import ttk#interface gráfica too

def conectar():
    return sqlite3.connect('usuarios.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
            id AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
            )
    ''')
    conn.commit()
    conn.close()
def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    if nome and email:
    conn = conectar()
    c = conn.cursor()
    c.execute('INSERT INTO usuarios(nome,email), VALUES(?,?)',(nome,email))
    messagebox.showinfo('oba','DADOS INSERIDOS COM SSSUUUUCCCEEEESSOOOO!')

    else:
    
        messagebox.showerror('AVISO','ALGO dEu ErRAdO')
    
def mostrar_usuario():
    for row in tree .get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert('tá aqui', 'end', values=(usuario[0],usuario[1],usuario[2]))
    conn.close()

def apaga_dado():
    dado_del = tree.curselection()
    if dado_del:
        user_id = tree.item(dado_del)('values')[0]
        conn=conectar()
        c=conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id = ?',(user_id))
        conn.commit()
        conn.close()
        messagebox.showinfo('quer apagar meSMo?','Dado DELETADO')
        mostrar_usuario

    else:
        messagebox.showerror('errou','OCORREU UM ERRO')

def editar():
    
    selecao = tree.curselection()
    
    if selecao
        user_id = tree.item(selecao)['values]'[0]]
        novo_nome = entry_nome.get()
        novo_email = entry_email.get()
        conn=conectar()
        c = conn.cursor()
        c.execute('UPDATE usuarios SET nome = ?, email = ?',(novo_email,novo_nome))
        conn.commit()
        conn.close()
        messagebox.showinfo('dnv man','DADOS atuALIzaDoS')
        mostrar_usuario

    
    else:
        messagebox.showwarning('ATENÇÃO','PREENCHA TODOS OS CAMPOS')
    
    
    else:
        messagebox.showerror('ERRO DE NOVO',' algo deu errrado (dnv)')
    

janela = tk.Tk()
janela.title('CRUD')

label_nome = tk.Label(janela, text='nome:',inserir_usuario)
label_nome.grid(row = 0,column=0,padx=10,pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

label_email = tk.Label(janela,text = 'E-mail:')
label_email.grid(row=1,column=0,padx=10,pady=10)

entry_email = tk.Entry(janela,text= 'E-mail:')
entry_email.grid(row=1,column=0,padx=10,pady=10)

btn_salvar = tk.Button(janela,text='Salvar')
btn_salvar.grid(row=2,column=0,padx=10,pady=10)

btn_deletar = tk.Button(janela,text='Deletar')
btn_deletar.grid(row=3,column=0,padx=10,pady=10)

btn_atualizar = tk.Button(janela,text='Atualizar',command=editar)
btn_atualizar.grid(row=4,column=0,padx=10,pady=10)

columns = ('ID','NOME','E-mail')

tree = ttk.Treeview(janela,columns,show = 'headings')
tree.grid(row=5,column=0,columnspan=2,padx=10, pady=10)


for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()






janela.mainloop()


