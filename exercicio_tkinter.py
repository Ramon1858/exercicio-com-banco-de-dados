import sqlite3
import tkinter as tk
from tkinter import messagebox

def  salvar():
    conn = sqlite3.connect('meu_db.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS dado(nome TEXT)')
    cursor.execute('INSERT INTO dado (nome) VALUES(?)',(input_1.get(),))
    n = input_1.get()
    print(n)
    conn.commit()
    conn.close()
    tk.messagebox.showinfo('salvar', 'DADOS SALVOS')    

def mostrar():
    lista.delete(0,tk.END)
    conn = sqlite3.connect('meu_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM dado')
    dado = cursor.fetchall()
    for dados in dado:
        lista.insert(tk.END, dados [0])
    conn.close()
    tk.messagebox.IGNORE = 'ignore'
    
def delete():
    dado_del = lista.curselection()
    if dado_del:
        nome = lista.get(dado_del)
        conn = sqlite3.connect('meu_db.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM dado WHERE nome = ?',(nome,))
        conn.commit()
        conn.close()
        tk.messagebox.showwarning('delete', 'DADOS DELETADOS')
        mostrar()
        
    
root = tk. Tk ()
root.geometry('300x400')
root.title('TESTE COM BANCO DE DADOS')

text = tk.Label(root,text='escreva algo')
text.pack()
#input - entry
input_1 = tk.Entry(root)
input_1.pack (pady=10)
#botão - button
btn = tk.Button(root,text='salvar',command=salvar)
btn.pack(padx=10)

btn_delete = tk.Button(root, text = 'delete', command=delete)
btn_delete.pack(padx=10,pady=25)

btn_mostra = tk.Button(root, text = 'Mostrar', command=mostrar)
btn_mostra.pack(padx=10,pady=20)

lista = tk.Listbox(root)
lista.pack(padx=10 , pady=30)

root.mainloop()