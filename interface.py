from tkinter import *

root=Tk()    
root.title("Observador de archivos")

ent1=Entry(root,font=40)
ent1.grid(row=2,column=2)
ent1.insert(0,"/Users/jhonrodriguez/PruebaTecnica/pruebatecnica/assets/billetesaTenerife.pdf" )

b1=Button(root,text="Seleccionar carpeta",font=40,command=lambda: buscarArchivo(ent1, 'pdf'), )
b1.grid(row=2,column=4, padx=0)

root.mainloop()