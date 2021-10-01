# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 08:46:07 2021

@author: enzoa
"""

from tkinter import *
import sqlite3

root = Tk()
root.title('Database')
root.geometry("350x400")

# Databases

# cria um banco de dados ou conecta a um
conn = sqlite3.connect('address_book.db')

# cria um cursor para navegar nos dados
cur = conn.cursor()

# cria a tabela do banco de dados
# cur.execute("""CREATE TABLE addresses (
#             first_name text,
#             last_name text,
#             address text,
#             city text,
#             state text,
#             zipcode integer
#             )""")


# cria a função para atualizar a edição de registro
def update():
    # cria um banco de dados ou conecta a um
    conn = sqlite3.connect('address_book.db')
    
    # cria um cursor para navegar nos dados
    cur = conn.cursor()
    
    record_id = delete_box.get()
    
    cur.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                
                WHERE oid = :oid
                """,
                {'first': f_name_editor.get(),
                 'last': l_name_editor.get(),
                 'address': address_editor.get(),
                 'city': city_editor.get(),
                 'state': state_editor.get(),
                 'zipcode': zipcode_editor.get(),
                 
                 'oid': record_id
                    
                    })
    
    # realiza mudanças no banco de dados
    conn.commit()
    
    # fecha a conexão com o banco de dados
    conn.close()

    # fecha a janela
    editor.destroy()

# cria função para editar um registro
def edit():
    # nova janela
    global editor
    editor = Tk()
    editor.title('Edit A Record')
    editor.geometry("350x200")

    # cria um banco de dados ou conecta a um
    conn = sqlite3.connect('address_book.db')
    
    # cria um cursor para navegar nos dados
    cur = conn.cursor()
    
    # edita um registro
    record_id = delete_box.get()
    cur.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cur
    
    # cria variáveis globais para as entradas
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    # create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    
    # create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # cria um botão de edição
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=120)
    
    # loop pelo registro
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])



    
    # realiza mudanças no banco de dados
    conn.commit()
    
    # fecha a conexão com o banco de dados
    conn.close()

# cria função para deletar um registor
def delete():
    # cria um banco de dados ou conecta a um
    conn = sqlite3.connect('address_book.db')
    
    # cria um cursor para navegar nos dados
    cur = conn.cursor()
    
    # deleta um registro
    cur.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    
    # realiza mudanças no banco de dados
    conn.commit()
    
    # fecha a conexão com o banco de dados
    conn.close()
    
    

# create submit function for database
def submit():
    # cria um banco de dados ou conecta a um
    conn = sqlite3.connect('address_book.db')
    
    # cria um cursor para navegar nos dados
    cur = conn.cursor()
    
    # insert into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
                  })
    
    # realiza mudanças no banco de dados
    conn.commit()
    
    # fecha a conexão com o banco de dados
    conn.close()
    
    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# create query function
def query():
    # cria um banco de dados ou conecta a um
    conn = sqlite3.connect('address_book.db')
    
    # cria um cursor para navegar nos dados
    cur = conn.cursor()

    # acessa o banco de dados
    cur.execute("SELECT *, oid FROM addresses") # * seleciona tudo    
    records = cur.fetchall() #fetchmany(50) or fetchone() 
    #print(records) # o print é apresentado somente no terminal
    
    # Loop pelo banco de dados
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)
    
    # realiza mudanças no banco de dados
    conn.commit()
    
    # fecha a conexão com o banco de dados
    conn.close()
    
    
    return

    
# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="ID Number")
delete_box_label.grid(row=9, column=0, pady=5)

# cria o botão de submissão
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# cria um botão de query
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# cria um botão de deletar
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# cria um botão de edição
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=134)


# realiza mudanças no banco de dados
conn.commit()

# fecha a conexão com o banco de dados
conn.close()

root.mainloop()