from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves():

    dicc = {'Pedro':'avatar', 'Elias': 'Azul123', 'Albertina': '456', 'Lucas': '12345',\
             'Ignacio': 'Rojo45', 'Emilia': '125', 'Daniel': '2090'}
    
    return dicc

def login_valido(usuario, clave):

    dicc = obtener_usuarios_claves()

    if usuario in dicc and clave == dicc[usuario]:
        messagebox.showinfo('', 'Usuario y Clave correctos')
    else:
        messagebox.showerror('','Algunos de los datos ingresados es Incorrecto')

def ventana_registro():

    ventana_registro = Tk()
    ventana_registro.title('Nuevo usuario')
    ventana_registro.resizable(0,0)
    ventana_registro.geometry('300x130')
    ventana_registro.config(bg='blue')
    ventana_registro.iconbitmap("IMG_Grupo_3.ico")

    nuevo_usuario = Label(ventana_registro, text='Nuevo usuario: ')
    nuevo_usuario.grid(row=0, column=0, padx=5, pady=10, sticky='e')

    usuario_registro = Entry(ventana_registro)
    usuario_registro.grid(row=0, column=1, pady=10, sticky='w')

    nueva_clave = Label(ventana_registro, text='Nueva clave: ')
    nueva_clave.grid(row=1, column=0, padx=5, pady=10, sticky='e')

    clave_registro = Entry(ventana_registro, show='*')
    clave_registro.grid(row=1, column=1, pady=10, sticky='w')

def crear_ventana():

    ventana = Tk()
    ventana.title('Login Grupo 3')
    ventana.resizable(0,0)
    ventana.geometry('300x130')
    ventana.config(bg='green')
    ventana.iconbitmap("IMG_Grupo_3.ico")

    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    label_usuario = Label(ventana, text='Usuario Alumno: ')
    label_usuario.grid(row=0, column=0, padx=5, pady=10, sticky='e')

    usuario = Entry(ventana)
    usuario.grid(row=0, column=1, pady=10, sticky='w')

    label_clave = Label(ventana, text='Clave: ')
    label_clave.grid(row=1, column=0, padx=5, pady=10, sticky='e')

    clave = Entry(ventana, show='*')
    clave.grid(row=1, column=1, pady=10, sticky='w')

    boton_enviar = Button(ventana, text="Ingresar", width=12, command=lambda:login_valido(usuario.get(), clave.get()))
    boton_enviar.grid(row=2, column=0, pady=10)

    boton_registrar = Button(ventana, text='Registrarse', command=lambda: ventana_registro())
    boton_registrar.grid(row=2, column=1, pady=10)

    ventana.mainloop()

def main():

   crear_ventana()

main()