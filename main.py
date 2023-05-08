import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw

# Crear la ventana principal
root = tk.Tk()

root.resizable(0,0)
root.title("Visualizador de Cambio de Temperatura")
root['background']='#569DAA'
width = 760 # Width 
height = 280 # Height

screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))



#! Metodos de dibujo de componentes 
 
# Crear una variable Tkinter para almacenar el valor del slider
valor_slider = tk.IntVar()

# Variable global para almacenar la imagen de la línea
imagen_tk = None

# Función para actualizar el valor en tiempo real del slider
def actualizar_valor(*args):
    valor = valor_slider.get()
    valor_texto.set(f"Estado del Agua a: {valor} °C")
    actualizar_imagen()


# Función para actualizar la imagen en función del valor del slider
def actualizar_imagen():
    global imagen_tk
    valor = valor_slider.get()
    if valor == 0:
        imagen = Image.open("i5.png")
    elif valor == 200:
        imagen = Image.open("i7.png")
    else:
        imagen = Image.new("RGB", (200, 200), (255, 255, 255))
    
    # Cambiar tamaño de imagen a 300x300
    imagen = imagen.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
        
    


# Crear un slider
slider = tk.Scale(root, from_=0, to=200, variable=valor_slider, orient=tk.HORIZONTAL, command=actualizar_valor,  bg="#569DAA", troughcolor="white")

valor_slider.set(20)  # Establecer valor inicial en 20 (temperatura ambiente)
slider.place(x=50, y=50, width=200, height=50)

# Crear una variable Tkinter para mostrar el valor en tiempo real del slider
valor_texto = tk.StringVar()
valor_texto.set("Estado del Agua a: 20 °C")
etiqueta_valor = tk.Label(root, textvariable=valor_texto)
etiqueta_valor.config(bg='#569DAA')
etiqueta_valor.pack(pady=10)

# Crear un cuadro de imagen
imagen = Image.new("RGB", (200, 200), (255, 255, 255))
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=imagen_tk)
etiqueta_imagen.pack(pady=20)

# Iniciar el bucle principal de la ventana de Tkinter
root.mainloop()