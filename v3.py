import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()

root.resizable(0,0)
root.title("Calculadora de Enfriamiento de Componentes")
root['background']='#569DAA'
width = 700 # Width 
height = 280 # Height

screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))



#! Metodos de dibujo de componentes 
 


# Crear un label para el textfield de ingreso
label1 = tk.Label(root, text="Ingrese la temperatura actual (en celsuis):")
label1.pack(pady=10)
label1.place(x=20, y=20)
label1['background']='#569DAA'

# Crear un textfield para ingresar un dato
entry1 = tk.Entry(root)
entry1.pack()
entry1.place(x=250, y=20)
entry1['background']='#577D86'

# Crear un label para el menú desplegable
label2 = tk.Label(root, text="Seleccione su componente:")
label2.pack(pady=10)
label2.place(x=20, y=60)
label2['background']='#569DAA'

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "orange", background= "white")


# Crear un menú desplegable con opciones
options = ["Seleccione una opcion","Intel Core i5-10300H", "Ryzen 5 5600H", "Intel Core i7-12700K"]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.current(0)
combo.pack()
combo.place(x=180, y=60, width=200, height=22)
combo['background']='#577D86'



# Crear un cuadro de imagen que cambie según la opción seleccionada
image1 = Image.open("i5.png")  # reemplazar con la ubicación de su propia imagen
resized_image1= image1.resize((275,197), Image.LANCZOS) # * 275,183 medidas fijas
photo1 = ImageTk.PhotoImage(resized_image1)
image2 = Image.open("ryzen 5.png")  # reemplazar con la ubicación de su propia imagen
resized_image2= image2.resize((275,197), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(resized_image2)
image3 = Image.open("i7.png")  # reemplazar con la ubicación de su propia imagen\
resized_image3= image3.resize((275,197), Image.LANCZOS) # * 275,183 medidas fijas   
photo3 = ImageTk.PhotoImage(resized_image3)
image4 = Image.open("empty.png")  # reemplazar con la ubicación de su propia imagen
resized_image4= image4.resize((275,197), Image.LANCZOS) # * 275,183 medidas fijas
photo4 = ImageTk.PhotoImage(resized_image4)


# Crear un label para el cuadro de imagen
label3 = tk.Label(root, text="Componente seleccionado:")
label3.pack(pady=10)
label3.place(x=400, y=20)
label3['background']='#569DAA'

image_label = tk.Label(root, image=photo4)
image_label.pack()
image_label.place(x=400, y=50)

# * funcion paa cambiar de imagen
def change_image(event):
    selection = combo.get()
    
    label4 = tk.Label(root, text="")
    label4.pack(pady=10)
    label4.place(x=20, y=170)
    label4['background']='#569DAA'
        
    if selection == "Seleccione una opcion":
        image_label.configure(image=photo4)
        label4.config(text="")
        
    elif selection == "Intel Core i5-10300H":
        image_label.configure(image=photo1)
        label4.config(text="El tiempo que tardará " + selection + " en enfriar es:")
        label4.place(x=21, y=170)
        
    elif selection == "Ryzen 5 5600H":
        image_label.configure(image=photo2)
        label4.config(text="El tiempo que tardará " + selection + " en enfriar es:                 ")
         
    elif selection == "Intel Core i7-12700K":
        label4.config(text="El tiempo que tardará " + selection + " en enfriar es:")
        image_label.configure(image=photo3)


combo.bind("<<ComboboxSelected>>", change_image)
selection = combo.get()



# Crear un cuadro de salida que no se pueda editar
output = tk.Text(root, height=10, state="disabled")
output.pack()
output.place(x=20, y=200, width= 350, height=50)
output['background']='#577D86'


# Crear un label para el botón de guardar
label5 = tk.Label(root, text="Presione el botón para calcular el tiempo en enfriar:")
label5.pack(pady=10)
label5.place(x=20, y=100)
label5['background']='#569DAA'


# Crear una función para guardar el dato ingresado
def calcular():
    data = entry1.get()
    output.configure(state="normal")
    output.delete("1.0", "end")
    output.insert("end", f": {data}")
    output.configure(state="disabled")

# Crear un botón para guardar el dato ingresado
button1 = tk.Button(root, text="Calcular", command=calcular, )
button1.pack(pady=10)
button1.place(x=20, y=130)
button1['background']='#577D86'




# Iniciar la ventana principal
root.mainloop()