import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
root.geometry("800x600")

# Crear figura y eje
fig = Figure(figsize=(3, 2), dpi=100)  # Cambiar el tamaño de la figura aquí
ax = fig.add_subplot(111)

# Datos de la gráfica
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Dibujar la gráfica
ax.plot(x, y)

fig.set_size_inches(3, 2)
# Crear lienzo de la figura en tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()
