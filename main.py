
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Crear la ventana principal
root = tk.Tk()

root.resizable(0,0)
root.title("Visualizador de Cambio de Estados del Agua")
root['background']='#569DAA'
width = 760 # Width 
height = 400 # Height

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


#Label para indicarle al usuario
labelEntry = tk.Label(root, text="Ingrese la temperatura:", font=("Arial", 10), fg="black", bg="#569DAA")
labelEntry2 = tk.Label(root, text="Entre -50 y 150", font=("Arial", 10), fg="black", bg="#569DAA")
labelEntry.place(x=20,y=10, width=170, height=20)
labelEntry2.place(x=20,y=28, width=170, height=20)

# Aqui ponemos el entry para poder ingresar la temperatura de manera manual
valor_manual = ttk.Entry(root)
valor_manual.place(x=180,y=20, width=30, height=20)

def actualizar_slider(event):
    try:
        valor = int(valor_manual.get())
        if valor >= slider["from"] and valor <= slider["to"]:
            slider.set(valor)
    except ValueError:
        pass

# Asignar la función al evento "Return/Enter" del campo de texto
valor_manual.bind("<Return>", actualizar_slider)



# Función para actualizar el valor en tiempo real del slider
def actualizar_valor(*args):
    valor = valor_slider.get()
    valor_texto.set(f"Estado del Agua a: {valor} °C")
    actualizar_imagen()


# Función para actualizar la imagen en función del valor del slider
def actualizar_imagen():
    global imagen_tk
    
    valor = valor_slider.get()
    if valor <= 0:
        imagen = Image.open("solido.jpg")
    elif valor > 0 and valor < 100:
        imagen = Image.open("liquido.png")
    else:
        imagen = imagen = Image.open("gaseoso.jpg")
    
    # Editando el tamaño de la imagen para ser editada en posicion
    imagen = imagen.resize((250, 200))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk
    #print(valor)
    
    #punto con el slider
    x = (valor + 50) / 200  # Normaliza el valor del slider en el rango de 0 a 1 para el eje x
    y = (100 - valor) / 100  # Normaliza el valor del slider en el rango de 0 a 1 para el eje y
    punto.set_data([x], [y])
    canvas.draw_idle()
        

#Label principal
titulo = tk.Label(root, text="Visualizador Cambio de Estados del Agua", font=("Arial", 16), fg="black", bg="#569DAA")
titulo.pack(pady=10)
titulo.place(x=300, y=35)


# Crear un slider
slider = tk.Scale(root, from_=-50, to=150, variable=valor_slider, orient=tk.HORIZONTAL, command=actualizar_valor,  bg="#569DAA", troughcolor="white")

valor_slider.set(20)  # Establecer valor inicial en 20 (temperatura ambiente)
slider.place(x=50, y=50, width=200, height=50)
slider.config(borderwidth=0, highlightbackground='#569DAA')


# Crear una variable Tkinter para mostrar el valor en tiempo real del slider
valor_texto = tk.StringVar()
valor_texto.set("Estado del Agua a: 20 °C")
etiqueta_valor = tk.Label(root, textvariable=valor_texto)
etiqueta_valor.config(bg='#569DAA')
etiqueta_valor.pack(pady=10)
etiqueta_valor.config(font=("Arial", 12))
etiqueta_valor.place(x=50, y=100)

# Crear un cuadro de imagen
imagen = Image.new("RGB", (200, 200), (255, 255, 255))
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=imagen_tk)
etiqueta_imagen.pack(pady=20)
etiqueta_imagen.place()
etiqueta_imagen.place(x=50, y=150, width=250, height=200)


#! Todo lo referente a la grafica

# Creamos la figura y el gráfico
fig = Figure(figsize=(1, 3), dpi=100, facecolor='#569DAA')
ax = fig.add_subplot(111)

# Datos de ejemplo para la línea ascendente
x = ["Sólido", "Líquido", "Gaseoso"]
y = [-20, 20 , 150]

# Dibujamos la línea ascendente
ax.plot(x, y, marker="o")

# Punto inicial en (0, 0)
punto, = ax.plot(0, 0, marker="o", color="red")  



fig.set_size_inches(1, 2)
ax.set_facecolor('#569DAA')  # Cambiar el color de fondo aquí (código hexadecimal)


# Creamos el lienzo de la figura
canvas = FigureCanvasTkAgg(fig, master=root)

canvas.get_tk_widget().configure(width=100, height=50)
canvas.draw()

# Mostramos el lienzo y empaquetamos la ventana
canvas.get_tk_widget().place(x=390, y=100,width=350, height=250)


# Iniciar el bucle principal de la ventana de Tkinter
root.mainloop()