from Tkinter import *
from string import capwords
import anydbm
import tkMessageBox
estado=0
def modificar():
    modificar=Toplevel(root)
    m=Label(modificar,text="Que Deseas Modificar!?")
    m.grid(column=1,row=1,sticky='W')
    state = IntVar()
    radio = Radiobutton(modificar, text="Nombre", variable=state, value=0)
    cc = Radiobutton(modificar, text="Apellido", variable=state, value=1)
    cc1 = Radiobutton(modificar, text="Telefono", variable=state, value=2)
    radio.grid(column=2,row=1,sticky='W')
    cc.grid(column=2,row=2,sticky='W')
    cc1.grid(column=2,row=3,sticky='W')
    radio = Radiobutton(modificar, text="Direccion", variable=state, value=3)
    cc = Radiobutton(modificar, text="Correo", variable=state, value=4)
    cc1 = Radiobutton(modificar, text="Nacimiento", variable=state, value=5)
    radio.grid(column=2,row=4,sticky='W')
    cc.grid(column=2,row=5,sticky='W')
    cc1.grid(column=2,row=6,sticky='W')
    cc1 = Radiobutton(modificar, text="Hobbie", variable=state, value=7,)
    cc1.grid(column=2,row=7,sticky='W')
    m=Label(modificar,text="Dato Nuevo: ")
    m.grid(column=1, row=8,sticky='W')
    dato= StringVar()
    g=Entry(modificar,bd=1,textvariable=dato)
    g.grid(column=2,row=8)
    def modi():
        au=[]
        datos=anydbm.open("registro","c")
        au=datos[str(contac.get())].split("\n")
        au[state.get()]=capwords(dato.get())
        datos[str(contac.get())]=au[0]+"\n"+au[1]+"\n"+au[2]+"\n"+au[3]+"\n"+au[4]+"\n"+au[5]+"\n"+au[6]+"\n"+au[7]+"\n"+au[8]+"\n"
        datos.close()
        if state.get()==0:
            datos=anydbm.open("nombres","c")
            au=datos[str(contac.get())].split("\n")
            au[state.get()]=capwords(dato.get())
            datos[str(contac.get())]=au[0]+" "+au[1]
            datos.close()
            actualizar()
        elif state.get()==1:
            datos=anydbm.open("nombres","c")
            au=datos[str(contac.get())].split("\n")
            au[state.get()]=capwords(dato.get())
            datos[str(contac.get())]=au[0]+" "+au[1]
            datos.close()
            actualizar()
        modificar.destroy()
    dcm = Button(modificar, text="Guardar", command=modi, width=20)
    dcm.grid(column=2,row=9)
def mostrar():
    mostrar1=Toplevel(root)
    def act():
        f=Label(mostrar,text=datos[str(contac.get())])
        f.grid(row=1,column=1)
        datos.close()
    mostrar=LabelFrame(mostrar1,text="Informacion del Contacto")
    mostrar.grid(row=1,column=1)
    datos=anydbm.open("registro","c")
    act()
    eli=Button(mostrar,text="Eliminar",command=eliminar)
    eli.grid(column=3,row=2)
    eli=Button(mostrar,text="Modificar",command=modificar)
    eli.grid(column=2,row=2)
def eliminar():
    datos=anydbm.open("nombres","c")
    del(datos[str(contac.get())])
    datos.close()
    m=anydbm.open("registro","c")
    del (m[str(contac.get())])
    m.close()
    tkMessageBox.showinfo("Eliminar", "Su Contacto ha sido eliminado con exito")
def registro():
    registro=Toplevel(root)
    def guardar():
        gf=anydbm.open('registro', 'c')
        nombre1=capwords(nombre.get())
        apellido1=capwords(apellido.get())
        telefono1=telefono.get()
        direccion1=capwords(direccion.get())
        correo1=correo.get()
        nacimiento1=nacimiento.get()
        genero1=genero.get()
        hobbie1=capwords(hobbie.get())
        gf[str(len(gf))]=nombre1+"\n"+apellido1+"\n"+telefono1+"\n"+direccion1+"\n"+correo1+"\n"+nacimiento1+"\n"+genero1+"\n"+hobbie1+"\n"
        gf.close()
        ag=anydbm.open("nombres","c")
        ag[str(len(ag))]=nombre1+" "+apellido1
        ag.close()
        actualizar()
        registro.destroy()
    m=Label(registro,text="Digite Su Nombre: ")
    m.grid(row=1,column=1,sticky='W')
    nombre= StringVar()
    g=Entry(registro,bd=1,textvariable=nombre)
    g.grid(row=1,column=2)
    
    m=Label(registro,text="Digite Su Apellido: ")
    m.grid(row=2,column=1,sticky='W')
    apellido= StringVar()
    g=Entry(registro,bd=1,textvariable=apellido)
    g.grid(row=2,column=2)
    
    m=Label(registro,text="Digite Su Telefono: ")
    m.grid(row=3,column=1,sticky='W')
    telefono= StringVar()
    g=Entry(registro,bd=1,textvariable=telefono)
    g.grid(row=3,column=2)
    
    m=Label(registro,text="Digite Su Direccion: ")
    m.grid(row=4,column=1,sticky='W')
    direccion= StringVar()
    g=Entry(registro,bd=1,textvariable=direccion)
    g.grid(row=4,column=2)
    
    m=Label(registro,text="Digite Su Correo: ")
    m.grid(row=5,column=1,sticky='W')
    correo= StringVar()
    g=Entry(registro,bd=1,textvariable=correo)
    g.grid(row=5,column=2)
    
    m=Label(registro,text="Digite Su Fecha de Nacimiento: ")
    m.grid(row=6,column=1,sticky='W')
    nacimiento= StringVar()
    g=Entry(registro,bd=1,textvariable=nacimiento)
    g.grid(row=6,column=2)
    
    m=Label(registro,text="Genero")
    m.grid(row=7,column=1,sticky='W')
    genero = StringVar()
    radio = Radiobutton(registro, text="Mujer", variable=genero, value="Mujer")
    cc = Radiobutton(registro, text="Hombre", variable=genero, value="Hombre")
    cc1 = Radiobutton(registro, text="Indefinido", variable=genero, value="Indefinido")
    radio.grid(row=7,column=2,sticky='W')
    cc.grid(row=8,column=2,sticky='W')
    cc1.grid(row=9,column=2,sticky='W')
    
    m=Label(registro,text="Digite Su Hobbie: ")
    m.grid(row=10,column=1,sticky='W')
    hobbie= StringVar()
    g=Entry(registro,bd=1,textvariable=hobbie)
    g.grid(row=10,column=2)
    
    dcm = Button(registro, text="Guardar", command=guardar, width=20)
    dcm.grid(row=11,column=2)

root=Tk(className="Agenda")

def actualizar():
    m=2
    datos=anydbm.open("nombres","c")
    for i in range(len(datos)):
        contactos = Radiobutton(root, text=datos[str(i)], variable=contac, value=i,command=mostrar)
        contactos.grid(row=m,column=1,sticky='W')
        m+=1
    datos.close()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo Contacto", command=registro)
filemenu.add_command(label="Modificar", command=modificar)
filemenu.add_command(label="Eliminar", command=eliminar)
filemenu.add_command(label="Actualizar", command=actualizar)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)
menubar.add_cascade(label="Archivo", menu=filemenu)
root.config(menu=menubar)

separador=Label(root, text="Contactos")
separador.grid(column=1,row=1)

contac= IntVar()
m=2
datos=anydbm.open("nombres","c")
for i in range(len(datos)):
    contactos = Radiobutton(root, text=datos[str(i)], variable=contac, value=i,command=mostrar)
    contactos.grid(row=m,column=1,sticky='W')
    m+=1
datos.close()
root.mainloop()
