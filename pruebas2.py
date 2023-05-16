import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Crear la ventana principal
root = tk.Tk()
root.geometry("800x600")
root.title("Visualizador de Cambio de Estados del Agua")
root.configure(background="#569DAA")

# Crear una variable Tkinter para almacenar el valor del slider
valor_slider = tk.IntVar()

# Variable global para almacenar la imagen de la línea
imagen_tk = None

# Función para actualizar el valor en tiempo real del slider
def actualizar_valor(*args):
    valor = valor_slider.get()
    valor_texto.set(f"Estado del Agua a: {valor} °C")
    actualizar_imagen()
    actualizar_punto()

# Función para actualizar la imagen en función del valor del slider
def actualizar_imagen():
    global imagen_tk
    
    valor = valor_slider.get()
    if valor <= 0:
        imagen = Image.open("solido.jpg")
    elif valor > 0 and valor < 100:
        imagen = Image.open("liquido.png")
    else:
        imagen = Image.open("gaseoso.jpg")
    
    # Editando el tamaño de la imagen para ser editada en posicion
    imagen = imagen.resize((200, 200))
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta_imagen.configure(image=imagen_tk)
    etiqueta_imagen.image = imagen_tk

# Función para actualizar la posición del punto en función del valor del slider
def actualizar_punto():
    valor = valor_slider.get()
    x = 0.3
    y = (valor - 20) / 130
    punto.set_data(x, y)
    canvas.draw_idle()

# Label principal
titulo = tk.Label(root, text="Visualizador Cambio de Estados del Agua", font=("Arial", 16), fg="black", bg="#569DAA")
titulo.pack(pady=10)

# Crear un slider
slider = tk.Scale(root, from_=-50, to=150, variable=valor_slider, orient=tk.HORIZONTAL, command=actualizar_valor, bg="#569DAA", troughcolor="white")
slider.set(20)  # Establecer valor inicial en 20 (temperatura ambiente)
slider.pack(pady=20)

# Crear una variable Tkinter para mostrar el valor en tiempo real del slider
valor_texto = tk.StringVar()
valor_texto.set("Estado del Agua a: 20 °C")
etiqueta_valor = tk.Label(root, textvariable=valor_texto, font=("Arial", 12), bg="#569DAA")
etiqueta_valor.pack(pady=10)

# Crear un cuadro de imagen
imagen = Image.new("RGB", (200, 200), (255, 255, 255))
imagen_tk = ImageTk.PhotoImage(imagen)
etiqueta_imagen = tk.Label(root, image=imagen_tk, bg="#569DAA")
etiqueta_imagen.pack(pady=20)

# Todo lo referente a la gráfica
fig = Figure(figsize=(2, 4), dpi=100)
ax = fig.add_subplot(111)

# Datos para la línea ascendente
x = ["Sólido", "Líquido", "Gaseoso"]
y = [-20, 20, 150]

# Dibujamos la línea ascendente
ax.plot(x, y, marker="o")

# Punto inicial en (0, 0)
punto, = ax.plot(0, 0, marker="o", color="red")

# Configuración de la gráfica
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

# Creamos el lienzo de la figura
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Actualizar posición del punto inicial
actualizar_punto()

# Iniciar el bucle principal de la ventana de Tkinter
root.mainloop()
