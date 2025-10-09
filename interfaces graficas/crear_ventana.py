'''
Ejercicio obligatorio de interfaces gráficas
'''

from tkinter import *
from tkinter import messagebox

def cadenaValida(cadena):
    valida = True

    if len(cadena)>25:
        valida=False

    i=0
    while valida and i<len(cadena):
        if not cadena[i].isalpha():
            valida = False
        i += 1
   
    return valida

def emailValido(email):
    valido = True

    if len(email)>20:
        valido=False
   
    if email.count('@') != 1 or email[0]=='@' or email[-1] == '@':
        valido = False    

    return valido

def validarDatos():
    
    nombre = cuadroDeNombre.get()
    apellido = cuadroDeApellido.get()
    email = cuadroDeEmail.get()
    
    if not cadenaValida(nombre):
        messagebox.showerror("Error", "El nombre no es válido.\nDebe tener solo letras y menos de 25 caracteres.")
        
    if not cadenaValida(apellido):
        messagebox.showerror("Error", "El apellido no es válido.\nDebe tener solo letras y menos de 25 caracteres.")
        
    if not emailValido(email):
        messagebox.showerror("Error", "El email no es válido.\nDebe tener una '@' en posición válida y menos de 20 caracteres.")

    if cadenaValida(nombre) and cadenaValida(apellido) and emailValido(email):
        messagebox.showinfo('Validador de datos', 'Los datos fueron enviados')


raiz=Tk()

raiz.title('Ingrese datos')

raiz.iconbitmap('interfaces graficas\Momo.ico')

raiz.geometry('500x300')

raiz.config(bg='green')

miLabel = Label(raiz, text='Hecho por Pedro Badii \n Texto en raiz')
miLabel.pack()

#-----Hasta acá la configuración de raiz------#

miFrame = Frame(raiz)
miFrame.pack(expand=True)

textoFrame = Label(miFrame, text='Esto está en el frame')
textoFrame.grid(row=0, column=0, columnspan=2)


miFrame.config(width='450', height='250')

miFrame.pack_propagate(True)

labelNombre=Label(miFrame, text='Nombre: ')
labelNombre.grid(row=1, column=0, sticky='e', padx=15)

miNombre=StringVar()
cuadroDeNombre=Entry(miFrame)
cuadroDeNombre.grid(row=1, column=1)

labelApellido=Label(miFrame, text='Apellido: ')
labelApellido.grid(row=2, column=0, sticky='e', padx=15)

cuadroDeApellido=Entry(miFrame)
cuadroDeApellido.grid(row=2, column=1,)

labelEmail=Label(miFrame, text='Dirección Email: ')
labelEmail.grid(row=3, column=0, sticky='w')

cuadroDeEmail=Entry(miFrame)
cuadroDeEmail.grid(row=3, column=1)

botonEnviar = Button(raiz, text='Enviar', command=validarDatos)
botonEnviar.pack()


raiz.mainloop()
